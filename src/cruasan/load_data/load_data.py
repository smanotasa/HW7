import pandas as pd

def load_data(file):
  try:
    df = pd.read_csv(file, index_col=0)
    return df
  except NameError:
    print('There is no such file')
