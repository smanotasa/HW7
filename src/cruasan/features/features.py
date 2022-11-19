#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def gen_dummy(df: pd.DataFrame, cols: list):
    dummies_df = pd.get_dummies(df, columns=cols)
    return dummies_df

def gen_bin(df: pd.DataFrame, cols: list):
    binary_df = pd.get_dummies(df, columns=cols)
    return dummies_df

