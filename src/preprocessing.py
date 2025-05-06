
from math import ceil
import numpy as np
import pandas as pd


def create_dummy_variables_from_categ_feature(df: pd.DataFrame, categ_feature: str):
    categories = list(df[categ_feature].unique())
    for category in categories:
        df[f"IS_{category.upper()[:3]}"] = (df[categ_feature] == category).astype('int')


def get_uniform_by_litho_train_set(df: pd.DataFrame, litho_col_name: str, nb_samples_by_litho: int):
    np.random.seed(42)
    LITHO = list(df[litho_col_name].unique())

    df_shuffled = df.sample(frac=1).reset_index(drop = True)
    train = pd.DataFrame()
    
    for litho in LITHO:
        df_litho_filtered = df_shuffled[df_shuffled[litho_col_name] == litho]
        litho_sample = df_litho_filtered.sample(nb_samples_by_litho) 
        train = pd.concat([train, litho_sample])
            
    return train.sample(frac=1).reset_index(drop=True)