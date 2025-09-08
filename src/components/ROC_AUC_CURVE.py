import os 
import sys 
from entity.artifact_entity import ModelTrainerArtifact
import matplotlib.pyplot as plt 
from sklearn.metrics import roc_curve, auc

class ROC_AUC_CURVE:
    def __init__(self,model_trainer_artifact : ModelTrainerArtifact):
        self.model_trainer_artifact = model_trainer_artifact

    def initiate_roc_auc_curve(self):
        report : dict = self.model_trainer_artifact.model_report
        plt.figure(figsize = (10,10))
        for model_name,metrics in report.items():

            fpr = metrics["fpr"]
            tpr = metrics["tpr"]            
            
            roc_auc = auc(fpr,tpr)
            plt.plot(fpr, tpr, label = f"{model_name} (AUC = {roc_auc : .2f})")

        plt.plot([0,1], [0,1], "k--", label = "Random Classifier")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC-AUC Curve")
        plt.legend(loc = 'lower right')
        plt.show()