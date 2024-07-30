from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def index():
    logging.info("Testing logging module")
    return "Welcome to the Machine Learning Project!"

if __name__ == '__main__':
    app.run(debug=True)