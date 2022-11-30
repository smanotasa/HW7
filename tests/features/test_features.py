from cruasan.features.features import gen_bin
from cruasan.features.features import gen_dummy
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

class Testfeatures(unittest.TestCase):
    
    def test_gen_dummy(self):
        data = pd.DataFrame({'col': ['Caucasian','Hispanic','Caucasian','Asian']})
        column = ['col'] 
        output = gen_dummy(data,column)
        expected_output = pd.DataFrame({'col_Caucasian': [1,0,1,0], 'col_Hispanic': [0,1,0,0]})
        assert_frame_equal(output,expected_output,check_dtype=False)
        
    def test_gen_bin(self):
        data = pd.DataFrame({'col': ['M','F','F','M']})
        column = ['col'] 
        output = gen_bin(data,column)
        expected_output = pd.DataFrame({'col_M': [1,0,0,1]})
        assert_frame_equal(output,expected_output,check_dtype=False)