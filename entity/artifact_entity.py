from dataclasses import dataclass
from typing import Dict

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
    model_report: Dict[str, Dict[str, float]]
    best_model_name: str
    best_score: float
    best_params: Dict[str, object]
    model_trainer_file_path: str
  

    