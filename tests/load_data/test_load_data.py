import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from cruasan.load_data.load_data import load_data

class Testload(unittest.TestCase):
    
    def test_load_data(self):
        file = 'sample_diabetes_mellitus_data.csv'
        output = load_data(file)
        expected_output = pd.read_csv(file, index_col=0)
        assert_frame_equal(output,expected_output,check_dtype=False)

Testload().test_load_data()
