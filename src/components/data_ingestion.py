import os
import sys
import pandas as pd 
import numpy as np 
from src.logger import logging
from src.exception import CustomExcetption
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
        
        
        
    def initiate_data_ingestion(self):
        '''
        this function is responsible for data ingestion
        '''
        
        try:
            df = pd.read_csv("dataset\data\stud.csv")
            logging.info("read the data as data frame")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("split the data into train test split")
            train_set, test_set = train_test_split(df,test_size=0.20, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("data ingestion has completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomExcetption(e,sys)
            
            
            
if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    
    
        
        
        