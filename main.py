import os 
import sys
from exception.exception import CustomException
from logger.logging import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from entity.config_entity import DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig
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
        model_trainer_config = ModelTrainerConfig(file_path_config = file_path_config)
        logging.info("Model Trainer Config")
        model_trainer = ModelTrainer(model_trainer_config = model_trainer_config, data_transformation_artifact = data_transformation_artifact)
        logging.info("Model Trainer Completed")
        model_trainer_artifact = model_trainer.initiate_model_trainer()
    except Exception as e:
        raise CustomException(e,sys)