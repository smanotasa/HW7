import unittest
import pandas as pd
from cruasan.score.score import roc_score
from sklearn.metrics import roc_auc_score

class Testsplit(unittest.TestCase):
    
    def test_split_data(self):
        train_pred = pd.DataFrame({'col1': [2,0]})
        y_train = pd.DataFrame({'col3': [1,8]})
        test_pred = pd.DataFrame({'col3': [1,3]})
        y_test = pd.DataFrame({'col1': [1,4]})
        self.assertEqual(roc_score(train_pred, y_train, test_pred, y_test),(roc_auc_score(y_train, train_pred),roc_auc_score(y_test, test_pred)))