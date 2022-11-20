from sklearn.metrics import roc_auc_score

<<<<<<< HEAD
def roc_score(train_pred, y_train, test_pred, y_test):
    score_train = roc_auc_score(y_train, train_pred)
    score_test = roc_auc_score(y_test, test_pred)
    return score_train, score_test
=======
def get_roc_auc_score(predictiontrain, y_train, predictiontest, y_test):
    score_train = roc_auc_score(y_train, train_pred)
    score_test = roc_auc_score(y_test, test_pred)
    return score_train, score_test
>>>>>>> 0bfd7ef5e969cab37f4f52202c55aad456288882
