import os
import sys
from src.logger import *
from src.exception import *
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_transformation import DataTransformationPipeline
from src.pipeline.stage_03_model_trainer import ModelTrainerPipeline


STAGE_NAME_1="Data Ingestion Stage"
try:
    logging.info(f"{STAGE_NAME_1} STARTED")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f"{STAGE_NAME_1} COMPLETED")
except Exception as e:
    logging.info("ERROR OCCURED IN DATA INGESTION")
    raise CustomException(e,sys)

STAGE_NAME_2="Data Transformation Stage"
try:
    logging.info(f"{STAGE_NAME_2} STARTED")
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logging.info(f"{STAGE_NAME_2} COMPLETED")
except Exception as e:
    logging.info("ERROR OCCURED IN DATA TRANSFORMATION")
    raise CustomException(e,sys)

STAGE_NAME_3="Model Trainer Stage"

try:
    logging.info(f"{STAGE_NAME_3} STARTED")
    model_trainer3=ModelTrainerPipeline()
    model_trainer3.main()
    logging.info(f"{STAGE_NAME_3} COMPLETED")
except Exception as e:
    logging.info("ERROR OCCURED IN MODEL TRAINING")
    raise CustomException(e,sys)

