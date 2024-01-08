import os
import sys
sys.path.insert(0, 'D:\Text_Summarizer\src')
from logger import logging
from exception import CustomException
from utils import *
from config.configuration import ConfigurationManager
from components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config3 = ConfigurationManager()
            model_evaluation_config3 = config3.get_model_evaluation_config()
            model_evaluation_config1 = ModelEvaluation(model_evaluation_config3)
            model_evaluation_config1.evaluate()
        except Exception as e:
            raise e
        

if __name__=='__main__':
    try:

        obj=ModelEvaluationPipeline()
        logging.info('STARTED')
        obj.main()
        logging.info('DONE')
    except Exception as e:
        logging.info("error has occured in training pipeline")
        raise CustomException(e,sys)