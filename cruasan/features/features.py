def gen_dummy(data, columns):
    return pd.get_dummies(data, columns=columns, drop_first=True)

def gen_bin(data, columns):
    return pd.get_dummies(data, columns=columns, drop_first=True)

