from src.makesense.logging import logger
from src.makesense.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e


logger.info("Logging has been configured.")
