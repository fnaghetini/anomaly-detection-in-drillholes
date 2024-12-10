import pandas as pd


def read_csv(file: str) -> pd.DataFrame():
    return pd.read_csv(file, sep=',', header=0, na_values=['-', ' '], encoding='latin-1', low_memory=False)
