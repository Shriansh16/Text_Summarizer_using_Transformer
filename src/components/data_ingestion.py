import os
import sys
import urllib.request as request
import zipfile
import gdown
sys.path.insert(0, 'D:\Text_Summarizer\src')
from logger import logging
from exception import CustomException
from utils import *
from pathlib import Path



class DataIngestion:
    def __init__(self,config):
        self.config=config
    def download_file(self):
        dataset_url=self.config.source_url
        zip_file_path=self.config.local_data_file
        os.makedirs('artifacts/data_ingestion',exist_ok=True)
        logging.info("downloading dataset from {url_path} into file {zip_file_path}")
        file_id=dataset_url.split('/')[-2]
        prefix_url='https://drive.google.com/uc?/export=download&id='
        gdown.download(prefix_url+file_id,zip_file_path)
        logging.info("dataset downloaded successfully")
    def unzipfile(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        logging.info("unzipping the downloaded file")
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logging.info("unzipping of file successfull")