import os
import sys
sys.path.insert(0, 'D:\Text_Summarizer\src')
from logger import logging
from exception import CustomException
from utils import *
from config.configuration import ConfigurationManager
from components.model_trainer import ModelTrainer


class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config1 = ConfigurationManager()
            model_trainer_config2 = config1.get_model_trainer_config()
            model_trainer_obj= ModelTrainer(model_trainer_config2)
            model_trainer_obj.train()
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    try:

        obj=ModelTrainerPipeline()
        logging.info('STARTED')
        obj.main()
        logging.info('DONE')
    except Exception as e:
        logging.info("error has occured in training pipeline")
        raise CustomException(e,sys)