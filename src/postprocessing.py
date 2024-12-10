import pandas as pd


def get_anomalies(df: pd.DataFrame(), df_pred: pd.DataFrame(), min_nb_votes=1) -> pd.DataFrame():
    # .sort_values(by=['VOTES'], ascending=False)
    anomaly_df = df_pred[df_pred['VOTES'] > min_nb_votes]
    feature_df = df.iloc[anomaly_df.index][['P2O5', 'CAO', 'FE2O3', 'SIO2', 'AL2O3', 'MGO']]
    final_cols = ['BHID', 'FROM', 'TO', 'P2O5', 'CAO', 'FE2O3', 'SIO2', 'AL2O3', 'MGO',
                  'LITHO', 'ISF_PRED', 'DBS_PRED', 'LOF_PRED', 'VOTES']
    return anomaly_df.join(feature_df)[final_cols].sort_values(by=['VOTES'], ascending=False)
