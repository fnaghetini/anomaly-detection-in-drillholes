import pandas as pd


def get_summary_table(table: pd.DataFrame()) -> pd.DataFrame():
    datadict = pd.DataFrame(table.dtypes, columns=['dType'])
    datadict["Valores Faltantes"] = table.isnull().sum()
    datadict["Valores Preenchidos"] = table.notnull().sum()
    datadict["Valores Únicos"] = table.nunique()
    return datadict


def calculate_stats_table(df: pd.DataFrame()) -> pd.DataFrame():
    stats = df.describe(percentiles=[0.1, 0.5, 0.995]).T
    stats['Amp'] = (df.max() - df.min()).tolist()  # amplitude (max = min)
    stats['S²'] = df.var().tolist()  # variância
    stats['Cᵥ'] = (df.std() / df.mean()).tolist()  # coeficiente de variação
    stats['Skew'] = df.skew().tolist()  # coeficiente de assimetria

    stats = stats.rename(columns={'mean': 'X̅', 'std': 'S', 'min': 'Min', 'max': 'Max'})

    return stats[['X̅', '50%', 'Min', '10%', '99.5%', 'Max', 'Amp', 'S²', 'S', 'Cᵥ', 'Skew']]
