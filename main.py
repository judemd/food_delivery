import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, processed_obj_file_path = data_transformation.initiate_data_transformation(train_data, test_data)
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_training(train_arr, test_arr))