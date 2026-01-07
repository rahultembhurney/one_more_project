import pandas as pd
import yaml
import os

with open("params.yaml", "r") as params:
    config = yaml.safe_load(params)

def test_check_empty_datastet():
    file_path = os.path.join(config['postgres_conn']['feature_store_path'],
                             config['postgres_conn']['feature_store_folder_name'],  
                             config['postgres_conn']['feature_store_file_name'],)
    df = pd.read_csv(file_path)
    flag = df.shape[0]
    assert flag>0, "Dataset is empty"

