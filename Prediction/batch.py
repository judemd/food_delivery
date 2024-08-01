import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.constants import *
from src.config.configuration import *
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException


PREDICTION_FOLDER = "batch_prediction"
PREDICTION_CSV = "prediction_csv"
PREDICTION_FILE = "output.csv"

