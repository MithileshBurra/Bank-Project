import os
import sys
import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

from exception.exception import CustomException
from logger.logging import logging

from entity.config_entity import DataTransformationConfig
from entity.artifact_entity import DataIngestionArtifact,DataTransformationArtifact

from utils.utils import save_object

class DataTransformation:
    def __init__(self,data_ingestion_artifact : DataIngestionArtifact, data_transformation_config : DataTransformationConfig):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_transformation_config = data_transformation_config

    def get_preprocessor(self,train_data : str, test_data : str):
        try:
            num_features = [feature for feature in train_data.columns if train_data[feature].dtype !='O']
            cat_features = [feature for feature in train_data.columns 
                if train_data[feature].dtype == 'O' and feature != "Target"]

            Transformer = ColumnTransformer(transformers = [
                    ("cat cols",OneHotEncoder(handle_unknown = "ignore"),cat_features),
                    ("num cols",StandardScaler(),num_features)
            ])

            pipeline = Pipeline(steps = [
                ("Transformer", Transformer),
                ("Smote", SMOTE(random_state = 42)),
            ])

            save_object(obj = pipeline, file_path = self.data_transformation_config.preprocessor_file_path)
            return pipeline
        except Exception as e:
            raise CustomException(e,sys)

    
    def initiate_data_transformation(self):
        
        try:
        
            
            train_data = pd.read_csv(self.data_ingestion_artifact.training_file_path)
            test_data = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            preprocessor = self.get_preprocessor(train_data = train_data, test_data = test_data)


            X_train_data = train_data.drop(['Target'],axis = 1)
            y_train_data = train_data['Target'].map({"yes":1,"no":0})

            X_test_data = test_data.drop(['Target'], axis = 1)
            y_test_data = test_data['Target'].map({"yes":1,"no":0})

            X_train_transformed,y_train_transformed = preprocessor.fit_resample(X_train_data,y_train_data)
            X_test_transformed = preprocessor.named_steps["Transformer"].transform(X_test_data)

            feature_names = preprocessor.named_steps["Transformer"].get_feature_names_out()

            X_train_df = pd.DataFrame(X_train_transformed, columns = feature_names)
            X_test_df = pd.DataFrame(X_test_transformed, columns = feature_names)

            transformed_train_data = pd.concat([X_train_df, pd.Series(y_train_transformed, name="Target")], axis=1)
            transformed_test_data = pd.concat([X_test_df, pd.Series(y_test_data, name="Target")], axis=1)

            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_train_file_path),exist_ok = True)
            transformed_train_data_df = transformed_train_data.to_csv(self.data_transformation_config.transformed_train_file_path, index = False,header = True)
            transformed_test_df = transformed_test_data.to_csv(self.data_transformation_config.transformed_test_file_path, index = False, header = True)


            data_transformation_artifact = DataTransformationArtifact( 
                transformed_train_file_path = self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path = self.data_transformation_config.transformed_test_file_path,
                preprocessor_file_path = self.data_transformation_config.preprocessor_file_path
            )

            return data_transformation_artifact


        except Exception as e:
            raise CustomException(e,sys)



        

        






