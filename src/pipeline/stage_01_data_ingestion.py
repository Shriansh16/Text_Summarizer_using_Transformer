import os
import sys
sys.path.insert(0, 'D:\Text_Summarizer\src')
from logger import logging
from exception import CustomException
from utils import *
from config.configuration import ConfigurationManager
from components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzipfile()
        except Exception as e:
            logging.info("ERROR OCCURED IN THE PIPELINE")
            raise CustomException(e,sys)