import logging
import os
from logging.handlers import RotatingFileHandler    
from datetime import datetime
import sys

time_stamp = datetime.now().strftime("%Y%m%d_%H_%M_%S")
log_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),'../')), '../'))
os.makedirs(os.path.join(log_dir, "LOGS"), exist_ok=True)
current_log_path = os.path.join(log_dir,"LOGS",f"{time_stamp}.log")

def configure_logger():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s]-[%(name)s]-[(%(level)s]-[%(message)s]')
    
    file_handler = RotatingFileHandler(current_log_path, encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter) 
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

configure_logger()
