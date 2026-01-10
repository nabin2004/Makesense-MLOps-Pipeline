from src.makesense.config.configuration import ConfigurationManager
from src.makesense.components.data_ingestion import DataIngestion
from src.makesense.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        config = ConfigurationManager()
        self.data_ingestion_config = config.get_data_ingestion_config()

    def initiate_data_ingestion(self):
        data_ingestion = DataIngestion(config=self.data_ingestion_config)
        data_ingestion.downlaod_file()
        data_ingestion.extract_zip_file()