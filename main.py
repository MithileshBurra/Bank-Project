import os 
import sys
from exception.exception import CustomException
from logger.logging import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from entity.config_entity import DataIngestionConfig,DataTransformationConfig
from entity.config_entity import FilePathConfig

if __name__ == "__main__":
    try:
        file_path_config = FilePathConfig()
        data_ingestion_config = DataIngestionConfig(file_path_config = file_path_config)
        logging.info("Data Ingetion Started")
        data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(data_ingestion_artifact)
        data_transformation_config = DataTransformationConfig(file_path_config = file_path_config)
        logging.info("Data Transformation Started")
        data_transformation = DataTransformation(data_ingestion_artifact = data_ingestion_artifact, data_transformation_config = data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)
    except Exception as e:
        raise CustomException(e,sys)