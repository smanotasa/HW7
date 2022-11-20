#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from sklearn.metrics import roc_auc_score

def get_roc_auc_score(predictiontrain, y_train, predictiontest, y_test):
    score_train = roc_auc_score(y_train, train_pred)
    score_test = roc_auc_score(y_test, test_pred)
    return score_train, score_test