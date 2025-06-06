import pandas as pd


def read_csv(file: str) -> pd.DataFrame:
    return pd.read_csv(file, sep=',', header=0, na_values=['-', ' '], encoding='latin-1', low_memory=False)


def save_to_csv(table: pd.DataFrame, out_dir: str) -> None:
    table.to_csv(out_dir, index=False, encoding='latin-1')
    print(f"Arquivo salvo com sucesso em: {out_dir}")