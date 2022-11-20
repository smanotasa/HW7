from sklearn.linear_model import LogisticRegression
import numpy as np

<<<<<<< HEAD

=======
>>>>>>> 0bfd7ef5e969cab37f4f52202c55aad456288882
model = LogisticRegression()

def train_model(x, y):
    model.fit(x, y)
    return x, y


def pred(train, test):
<<<<<<< HEAD
    train_pred = train['predictions'] = np.squeeze(model.predict_proba(train)[:, 1])
    test_pred = test['predictions'] = np.squeeze(model.predict_proba(test)[:, 1])
=======
    predictiontrain = train['predictions'] = np.squeeze(model.predict_proba(train)[:, 1])
    predictiontest = test['predictions'] = np.squeeze(model.predict_proba(test)[:, 1])
>>>>>>> 0bfd7ef5e969cab37f4f52202c55aad456288882
    return train, test, train_pred, test_pred