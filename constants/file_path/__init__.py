import os 

TARGET_COLUMN : str = ""
PIPELINE_NAME : str ="BANK_PROJECT"
ARTIFACT_DIR_NAME :str ="Artifacts"
DATASET_DIR_NAME :str = "Dataset"
DATASET_NAME : str = "BankData.csv"



DATA_INGESTION_DIR_NAME :str = "data_ingestion"
DATA_INGESTED_DIR : str = "ingested"
TRAINING_FILE_NAME :str = "train.csv"
TEST_FILE_NAME :str ="test.csv"
DATA_TRAIN_TEST_SPLIT_RATIO = 0.3

PREPROCESSOR_DIR_NAME = "Preprocessor"
PREPROCESSOR_FILE_NAME = "Preprocessor.pkl"
TRANSFORMED_DIR_NAME = "Transformed"
TRANSFORMED_TRAIN_FILE_NAME = "Transformed_train.csv"
TRANSFORMED_TEST_FILE_NAME = "Transformed_test.csv"


MODEL_TRAINER_DIR_NAME = "Model"
MODEL_TRAINER_FILE_NAME = "ModelTrainer.pkl"

