import numpy as np

def drop_nan(column,df):
    for i in column:
        df = df.dropna(subset=[i])
    return df

def fill_mean(df, column):
    df[column] = df[column].fillna(np.mean(df[column]))
    return df

