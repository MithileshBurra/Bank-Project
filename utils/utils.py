import os
import sys

from exception.exception import CustomException
from logger.logging import logging
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, f1_score,recall_score,average_precision_score,classification_report,accuracy_score

def save_object(obj, file_path: str):

    try:
        os.makedirs(os.path.dirname(file_path),exist_ok =True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model_name = list(models.keys())[i]
            para = param[model_name]
            print(f"Printing Classification Report of {model_name}")
            grid = GridSearchCV(model,para,cv=3,verbose=3,n_jobs=-1)
            grid.fit(X_train,y_train)

            best_model = grid.best_estimator_
            best_params = grid.best_params_
            y_pred = best_model.predict(X_test)
            y_prob = best_model.predict_proba(X_test)[:,1]
            precision = precision_score(y_test,y_pred)
            f1score = f1_score(y_test,y_pred)
            recallscore = recall_score(y_test,y_pred)
            accuracyscore = accuracy_score(y_test,y_pred)
            auc_pr = average_precision_score(y_test,y_prob)

            ##print(f"Classification Report of {model_name}\n {classification_report(y_test,y_pred)}")
            report[model_name]={
                "Precision_score" : precision,
                "F1_score" : f1score,
                "Recall_score" : recallscore,
                "AUC_PR" : auc_pr,
                "Accuracy" : accuracyscore,
                "best_params" : best_params
            }
        return report




    except Exception as e:
        raise CustomException(e,sys)
