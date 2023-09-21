import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from catboost import CatBoostClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts", "classifier_model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Entered model trainer")
            logging.info("Spliting training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            logging.info("Done Spliting training and test input data")
            logging.info("Exploring the classifier algorithms")
            models = {
                "Logistic Regression": LogisticRegression(),
                "Naive bayes": GaussianNB(),
                "CatBoost Classifier": CatBoostClassifier(),
            }
            params= {

                             'Logistic Regression': {
                            "penalty": ['l1', 'l2'],
                            'C': [0.01, 0.1, 1.0],
                            'max_iter': [100, 200, 300]
                        },
                        

                        'Naive bayes': {},

                        'CatBoost Classifier': {
                            'iterations': [100, 200],  # Number of boosting iterations
                            'learning_rate': [0.01, 0.1, 1.0],  # Learning rate
                            'depth': [6, 8, 10],  # Depth of the trees
                            'l2_leaf_reg': [1, 3, 5],  # L2 regularization coefficient
                            }
                     }       
           
            logging.info("Evaluating classifier algorithms")
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            print(model_report)
            logging.info("choosing best classifier algorithm")
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = accuracy_score(y_test, predicted)
            return r2_square,best_model_name
                       
        except Exception as e:
            raise CustomException(e,sys)