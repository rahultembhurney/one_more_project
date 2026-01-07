import psycopg2
import yaml
from pathlib import Path
import sys 
import pandas as pd
import os

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

from src.logger import logger

def load_yaml():
    with open("params.yaml", "r") as params:
        config = yaml.safe_load(params)
    return config


def extract_file_from_table():
    try:
        logger.info("loading yaml file")
        config = load_yaml()

        logger.info("Importing connection details")

        logger.info("Establishing connection..")
        conn = psycopg2.connect(dbname=config['postgres_conn']['dbname'],
                                user=config['postgres_conn']['user'],
                                password=config['postgres_conn']['password'],
                                host=config['postgres_conn']['host'],
                                port=config['postgres_conn']['port'])
        logger.info("Connection established successfully")
        
        logger.info("extracting table/s")

        # postgres_uri = f"postgresql://config['postgres_conn']['user']:password=config['postgres_conn']['password']@host=config['postgres_conn']\
        # ['host']:port=config['postgres_conn']['port']/config['postgres_conn']['dbname']"
        # conn = postgres_uri
        df = pd.read_sql_query(f"SELECT * FROM {config['postgres_conn']['schema_name']}.{config['postgres_conn']['table_name']}", conn)

        logger.info("making directory for Artifact folder")
        folder_path = os.path.join(project_root, config['postgres_conn']['feature_store_path'])
        os.makedirs(folder_path, exist_ok=True)

        logger.info("making path for feature store data")
        feature_file_path = os.path.join(folder_path, config['postgres_conn']['feature_store_folder_name'])
        os.makedirs(feature_file_path, exist_ok=True)


        logger.info("exporting data")
        df.to_csv(f"{feature_file_path}/{config['postgres_conn']['feature_store_file_name']}", index=False)

        logger.info("closing connection")
        conn.close()
    except Exception as e:
        logger.info(f"Error Occured: {e}")

if __name__ == "__main__":  
    extract_file_from_table()
        
