import os
import sys
sys.path.insert(0, 'D:\Text_Summarizer\src')
from logger import logging
from exception import CustomException
from utils import *
from config.configuration import ConfigurationManager
from components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config1 = ConfigurationManager()
            data_transformation_config = config1.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise CustomException(e,sys)

