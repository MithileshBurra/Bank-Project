import os 
import sys 
import pandas as pd
import numpy as np
from exception.exception import CustomException
from logger.logging import logging
from entity.config_entity import DataIngestionConfig
from sklearn.model_selection import train_test_split
from entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def split_data_as_train_test(self,dataframe : pd.DataFrame):
        try:
        
            train_data,test_data = train_test_split(dataframe,test_size = self.data_ingestion_config.train_test_split_ratio,random_state = 42)
            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path),exist_ok = True)
            train_data.to_csv(self.data_ingestion_config.training_file_path,index = False,header = True)
            test_data.to_csv(self.data_ingestion_config.test_file_path, index = False, header = True)

            logging.info("Train and Test Datasets Added")
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion Started")

            df = pd.read_csv("/Users/mithileshgoud/Downloads/Bank_Marketing_dataset.csv")
            logging.info("Dataset Read")
            os.makedirs(os.path.dirname(self.data_ingestion_config.data_file_path),exist_ok = True)
            df.to_csv(self.data_ingestion_config.data_file_path,index = False, header = True)
            logging.info("DataSet Added")
            self.split_data_as_train_test(dataframe = df)

            data_ingestion_artifact = DataIngestionArtifact(
                                                            training_file_path=self.data_ingestion_config.training_file_path,
                                                            test_file_path=self.data_ingestion_config.test_file_path
                                                            )

            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e,sys)






