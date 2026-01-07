import pandas as pd

def load_dataset(file_path:str):
    df = pd.read_csv(file_path)
    return df

def check_empty_datastet(df:pd.DataFrame):
    flag = df.value_counts().sum()
    assert(flag>0, "Dataset is empty")