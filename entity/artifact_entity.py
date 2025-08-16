from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    training_file_path:str 
    test_file_path:str
@dataclass
class DataTransformationArtifact:
    preprocessor_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str
