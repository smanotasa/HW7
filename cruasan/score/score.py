#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from sklearn.metrics import roc_auc_score

def get_roc_auc_score(trained: tuple):

    y_train, y_test, y_train_pred_proba, y_test_pred_proba = trained
    
    train_auc_score = roc_auc_score(y_train, y_train_pred_proba)
    test_auc_score = roc_auc_score(y_test, y_test_pred_proba)
    
    return train_auc_score, test_auc_score    

