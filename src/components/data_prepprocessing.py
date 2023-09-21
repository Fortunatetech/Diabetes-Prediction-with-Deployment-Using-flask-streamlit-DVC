import sys
import os
import numpy as np 
import pandas as pd
from scipy import stats
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from src.exception import CustomException
from src.logger import logging


@dataclass
class DataPreprocessingConfig:
    train_data_path_cleaned: str=os.path.join('artifacts',"train_cleaned.csv")
    test_data_path_cleaned: str=os.path.join('artifacts',"test_cleaned.csv")

class DataPreprocessing:
    def __init__(self):
        self.preprocessing_config=DataPreprocessingConfig()
    
    def initiate_data_preprocessing(self):
        logging.info("Entered the data preprocessing method or component")
        try:
            train_df=pd.read_csv("artifacts/train.csv")
            test_df=pd.read_csv("artifacts/test.csv")
        
            logging.info('Read the train and test dataset as dataframe')

            logging.info('Cleaning both train and test dataframe')

            threshold=3.0
            # Calculate the Z-scores for each numeric column intrain_df
            z_scores_train = np.abs(stats.zscore(train_df.select_dtypes(include=['number'])))

            # Create a DataFrame to store the Z-scores in train df
            z_score_train_df = pd.DataFrame(z_scores_train, columns=train_df.select_dtypes(include=['number']).columns)

            # Find and store the rows with outliers for each numeric feature
            outlier_indices_train = np.where( z_scores_train > threshold)
            outlier_rows_train_df = set(outlier_indices_train[0])  # Get unique row indices with outliers

            # Drop the outlier rows in train df
            train_df = train_df.drop(index=list(outlier_rows_train_df))

            
            logging.info("Cleaning completed for train data")

             # Calculate the Z-scores for each numeric column in test df
            z_scores_test = np.abs(stats.zscore(test_df.select_dtypes(include=['number'])))

            # Create a DataFrame to store the Z-scores
            z_score_test_df = pd.DataFrame(z_scores_test, columns=test_df.select_dtypes(include=['number']).columns)

            # Find and store the rows with outliers for each numeric feature
            outlier_indices_test = np.where( z_scores_test > threshold)
            outlier_rows_test_df = set(outlier_indices_test[0])  # Get unique row indices with outliers

            # Drop the outlier rows
            test_df = train_df.drop(index=list(outlier_rows_test_df))

            logging.info("Cleaning completed for test data")

            os.makedirs(os.path.dirname(self.preprocessing_config.train_data_path_cleaned),exist_ok=True)
            logging.info('directory created for cleaned data')


            train_df.to_csv(self.preprocessing_config.train_data_path_cleaned,index=False,header=True)
            logging.info('Cleaned trained data saved')
            test_df.to_csv(self.preprocessing_config.test_data_path_cleaned,index=False,header=True)
            logging.info('Cleaned test data saved')

            return train_df, test_df
            logging.info("data Preprocessing completed")        
        
        except Exception as e:
            raise CustomException(e,sys)
