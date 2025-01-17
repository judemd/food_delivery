import logging
import os, sys
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
file_name = f"log_{CURRENT_TIMESTAMP}.log"

log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(filename=log_file_path, 
                    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

