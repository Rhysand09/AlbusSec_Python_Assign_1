import pandas as pd

def clean_data(file_name):
    df = pd.read_csv(file_name)
    df.drop_duplicates(inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df
