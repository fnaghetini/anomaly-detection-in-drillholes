import pandas as pd

PK = ['BHID', 'FROM', 'TO']
COORDS = ['X', 'Y', 'Z']
ANALYTES = ['P2O5', 'CAO', 'FE2O3', 'SIO2', 'AL2O3', 'MGO']
MODEL_COLS = ['ANOMALY_SCORE', 'IS_ANOMALY']
FINAL_COLS = PK + COORDS + ANALYTES + ['LITO'] + MODEL_COLS


def get_anomalies(df: pd.DataFrame, df_pred: pd.DataFrame) -> pd.DataFrame:
    anomaly_df = df_pred[df_pred['IS_ANOMALY'] == 1]
    feature_df = df.iloc[anomaly_df.index][ANALYTES]
    return anomaly_df.join(feature_df)[FINAL_COLS].sort_values(by=['ANOMALY_SCORE'], ascending=True)
