import numpy as np
from collections import defaultdict


def kfold_split(num_objects, num_folds):
    """Split [0, 1, ..., num_objects - 1] into equal num_folds folds (last fold can be longer) and returns num_folds train-val
       pairs of indexes.

    Parameters:
    num_objects (int): number of objects in train set
    num_folds (int): number of folds for cross-validation split

    Returns:
    list((tuple(np.array, np.array))): list of length num_folds, where i-th element of list contains tuple of 2 numpy arrays,
                                       the 1st numpy array contains all indexes without i-th fold while the 2nd one contains
                                       i-th fold
    """
    fold_size = num_objects // num_folds

    def test(i):
        return range(i * fold_size, num_objects if i + 1 == num_folds else (i + 1) * fold_size)

    return [(np.array([*(set(range(num_objects)) - set(test(i)))]), np.array(test(i))) for i in range(num_folds)]


def knn_cv_score(X, y, parameters, score_function, folds, knn_class):
    """Takes train data, counts cross-validation score over grid of parameters (all possible parameters combinations)

    Parameters:
    X (2d np.array): train set
    y (1d np.array): train labels
    parameters (dict): dict with keys from {n_neighbors, metrics, weights, normalizers}, values of type list,
                       parameters['normalizers'] contains tuples (normalizer, normalizer_name), see parameters
                       example in your jupyter notebook
    score_function (callable): function with input (y_true, y_predict) which outputs score metric
    folds (list): output of kfold_split
    knn_class (obj): class of knn model to fit

    Returns:
    dict: key - tuple of (normalizer_name, n_neighbors, metric, weight), value - mean score over all folds
    """
    result = dict()
    for normalizer in parameters['normalizers']:
        for k in parameters['n_neighbors']:
            for metr in parameters['metrics']:
                for weight in parameters['weights']:
                    scores = []
                    for fold in folds:
                        X_train = X[fold[0]]
                        X_test = X[fold[1]]
                        y_train = y[fold[0]]
                        y_test = y[fold[1]]
                        scaler = normalizer[0]
                        X_train_scaled, X_test_scaled = X_train, X_test
                        if scaler is not None:
                            scaler.fit(X_train)
                            X_train_scaled = scaler.transform(X_train)
                            X_test_scaled = scaler.transform(X_test)
                        neigh = knn_class(n_neighbors=min(len(X_train_scaled), k), weights=weight, metric=metr)
                        neigh.fit(X_train_scaled, y_train)
                        y_pred = neigh.predict(X_test_scaled)
                        scores.append(score_function(y_test, y_pred))
                    result[(normalizer[1], k, metr, weight)] = np.mean(scores)
    return result
