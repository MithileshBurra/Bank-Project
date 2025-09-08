**Bank Customer Prediction Project**

This project implements a complete Machine Learning pipeline to predict customer outcomes (e.g., churn, loan default, or behavior) using various ML models. It follows a modular production-grade pipeline with configurable entities, artifacts, logging, and exception handling.

**Features**

Data Ingestion: Reads and splits raw data into training and test sets.

Data Transformation: Preprocessing with scaling, encoding, and transformation pipelines.

Model Training: Trains multiple ML models including:

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting

AdaBoost

KNN

Naive Bayes

Hyperparameter Tuning: Uses GridSearchCV for best model parameters.

Evaluation Metrics: Computes Precision, Recall, F1-score, AUC-PR, ROC-AUC.

Model Persistence: Saves best model with joblib/pickle.

Visualization: Plots ROC-AUC curve for comparison across models.

Modular Design: Organized with config_entity, artifact_entity, exception, logger, and utils.
