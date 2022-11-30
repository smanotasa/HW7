import unittest
import pandas as pd
from cruasan.split_data.split_data import split_data

class Testsplit(unittest.TestCase):
    
    def test_split_data(self):
        X = pd.DataFrame({'col1': ['A','B','C','D','E'] , 'col2': [1,2,3,4,5]})
        y = pd.DataFrame({'col3': [1,0,0,1,0]})
        split = split_data(X,y)
        assert split[0].shape == (4, 2)
        assert split[1].shape == (1, 2)
        assert split[2].shape == (4, 1)
        assert split[3].shape == (1, 1)