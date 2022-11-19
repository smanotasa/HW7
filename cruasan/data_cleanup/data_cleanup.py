#data_cleanup

#Functions

def drop_nan(column,df):
    for i in column:
        df = df.dropna(subset=[i])
    return df

def fill_mean(column):
    df[column].fillna(value=df[column].mean(),inplace=True)
    return df


