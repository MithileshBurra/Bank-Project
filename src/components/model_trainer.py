import os
import sys
import pandas as pd
import numpy as np
from entity.config_entity import ModelTrainerConfig
from entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from exception.exception import CustomException
from logger.logging import logging
from utils.utils import save_object,evaluate_model
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier,AdaBoostClassifier


class ModelTrainer:
    def __init__(self,model_trainer_config : ModelTrainerConfig,data_transformation_artifact : DataTransformationArtifact):
        self.model_trainer_config = model_trainer_config
        self.data_transformation_artifact = data_transformation_artifact

    def train_model(self,X_train,y_train,X_test,y_test):
        try:
            models = {
                "Logistic Regression": LogisticRegression(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "AdaBoost": AdaBoostClassifier(),
                "KNN": KNeighborsClassifier(),
                "Navie Bayes": GaussianNB()
            }

            params={
                "Logistic Regression":{},
                "Decision Tree": {
                    'criterion':['gini', 'entropy', 'log_loss'],
                    'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    'criterion':['gini', 'entropy', 'log_loss'],
                    'n_estimators': [8,16,32,128,256]
                },
                "Gradient Boosting":{
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.85,0.9],
                    'n_estimators': [8,16,32,64,128,256]
                },
                
                "AdaBoost":{
                    'learning_rate':[.1,.01,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "KNN":{
                    'n_neighbors' : [3,5,7,9,11],
                    'weights':['uniform', 'distance']
                },
                "Navie Bayes" :{}
                
            }

            model_report : dict = evaluate_model(X_train,y_train,X_test,y_test,models,params)
            
            best_model_name, best_metrics = max(model_report.items(), key = lambda item: item[1]["F1_score"])
            print(f"The best model is {best_model_name}")
            best_score = best_metrics["F1_score"]
            best_model = models[best_model_name]
            best_params = best_metrics["best_params"]
            os.makedirs(os.path.dirname(self.model_trainer_config.model_trainer_dir_name),exist_ok = True)
            save_object(obj = best_model, file_path = self.model_trainer_config.model_trainer_file_path)

            model_trainer_artifact = ModelTrainerArtifact(
                model_report=model_report,
                best_model_name=best_model_name,
                best_score=best_score,
                best_params = best_params,
                model_trainer_file_path=self.model_trainer_config.model_trainer_file_path,
            )
             

            return model_trainer_artifact
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_model_trainer(self):
        try:
            training_data = pd.read_csv(self.data_transformation_artifact.transformed_train_file_path)
            test_data = pd.read_csv(self.data_transformation_artifact.transformed_test_file_path)

            X_train = training_data.drop(["Target"],axis = 1)
            y_train = training_data['Target']
            X_test = test_data.drop(["Target"], axis = 1)
            y_test = test_data['Target']

            artifact = self.train_model(X_train,y_train,X_test,y_test)
            
            for model_name, metrics in artifact.model_report.items():
                print(f"Model Name = {model_name}")
                print(metrics)

        except Exception as e:
            raise CustomException(e,sys)
