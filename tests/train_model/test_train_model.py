from cruasan.train_model.train_model import train_model
from sklearn.linear_model import LogisticRegression
import unittest
import pandas as pd


class Test_train(unittest.TestCase):
    
    def test_train_model(self):
        x = pd.DataFrame({'col1': [1,2,4,5,6] , 'col2': [1,2,3,4,5]})
        y = pd.DataFrame({'col3': [1,0,0,1,0]})
        output = train_model(x,y)
        expected_output = LogisticRegression().fit(x, y)
        self.assertEqual(output,expected_output)
