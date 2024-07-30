from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def index():
    
    try:
        raise Exception("Testing custom exception")
    except Exception as e:
        ML = CustomException(e, sys)
    logging.info(ML.error_message)
        
    logging.info("Testing logging module")
    return "Welcome to the Machine Learning Project!"

if __name__ == '__main__':
    app.run(debug=True)