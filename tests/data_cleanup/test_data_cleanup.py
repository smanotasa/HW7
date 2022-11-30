from cruasan.data_cleanup.data_cleanup import drop_nan
from cruasan.data_cleanup.data_cleanup import fill_mean

import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

class Testdatacleanup(unittest.TestCase):
    
    def test_drop_nan(self):
        column = ['col'] 
        df = pd.DataFrame({'col': [0,5,10, np.nan]})
        output = drop_nan(column,df)
        expected_output = pd.DataFrame({'col': [0,5,10]})
        assert_frame_equal(output,expected_output,check_dtype=False)
        
    def test_fill_mean(self):
        df = pd.DataFrame({'col': [0,5,10, np.nan]})
        column = ['col'] 
        output = fill_mean(df,column)
        expected_output = pd.DataFrame({'col': [0,5,10,5]})
        assert_frame_equal(output,expected_output,check_dtype=False)