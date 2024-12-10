import pandas as pd


def create_dummy_variables_from_categ_feature(df: pd.DataFrame(), categ_feature: str):
    categories = list(df[categ_feature].unique())
    for category in categories:
        df[f"IS_{category}"] = (df[categ_feature] == category).astype('int')
