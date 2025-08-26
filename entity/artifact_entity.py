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
@dataclass
class ModelTrainerArtifact:
    model_report: dict[str, dict[str, float]]
    best_model_name: str
    best_score: float
    best_params: dict[str, object]
    model_trainer_file_path: str

    