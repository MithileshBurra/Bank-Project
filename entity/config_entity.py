import os 
import sys
from constants import file_path

class FilePathConfig:
    def __init__(self):
        self.artifact_name = file_path.ARTIFACT_DIR_NAME
        
class DataIngestionConfig:
    def __init__(self,file_path_config : FilePathConfig):
        self.ingestion_dir : str = os.path.join(file_path_config.artifact_name,file_path.DATA_INGESTION_DIR_NAME)
        self.training_file_path : str = os.path.join(self.ingestion_dir,file_path.TRAINING_FILE_NAME)
        self.test_file_path : str = os.path.join(self.ingestion_dir,file_path.TEST_FILE_NAME)
        self.train_test_split_ratio : str = file_path.DATA_TRAIN_TEST_SPLIT_RATIO
        self.data_file_path :str = os.path.join(file_path.DATASET_DIR_NAME, file_path.DATASET_NAME)

class DataTransformationConfig:
    def __init__(self, file_path_config: FilePathConfig):

        self.preprocessor_dir = os.path.join(file_path_config.artifact_name, file_path.PREPROCESSOR_DIR_NAME)
        self.preprocessor_file_path = os.path.join(self.preprocessor_dir, file_path.PREPROCESSOR_FILE_NAME)
        self.transformed_dir = os.path.join(file_path_config.artifact_name,file_path.TRANSFORMED_DIR_NAME)
        self.transformed_train_file_path = os.path.join(self.transformed_dir,file_path.TRANSFORMED_TRAIN_FILE_NAME)
        self.transformed_test_file_path = os.path.join(self.transformed_dir,file_path.TRANSFORMED_TEST_FILE_NAME)

class ModelTrainerConfig:

    def __init__(self, file_path_config : FilePathConfig):

        self.model_trainer_dir_name = os.path.join(file_path_config.artifact_name, file_path.MODEL_TRAINER_DIR_NAME)
        self.model_trainer_file_path = os.path.join(file_path_config.artifact_name, file_path.MODEL_TRAINER_FILE_NAME)
