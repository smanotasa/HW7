from sklearn.model_selection import train_test_split

def split_data(X,y):
    seed = 1
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = seed, train_size = .80)
    return X_train, X_test, y_train, y_test