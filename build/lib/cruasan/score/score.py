from sklearn.metrics import roc_auc_score

def roc_score(train_pred, y_train, test_pred, y_test):
    score_train = roc_auc_score(y_train, train_pred)
    score_test = roc_auc_score(y_test, test_pred)
    return score_train, score_test

