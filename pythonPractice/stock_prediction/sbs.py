from sklearn.base import clone
from itertools import combinations
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class SBS():
    """
    class for Sequential Backward Selection (SBS)
    """
    def __init__(self, estimator, k_features, scoring=accuracy_score,
                 test_size=0.25, random_state=1):
        """
        Parameters
        ----------
        scoring :
        """
        self.scoring = scoring
        self.estimator = clone(estimator)
        self.k_features = k_features
        self.test_size = test_size
        self.random_state = random_state

    def fit(self, X, y):
        #split training data and test data
        X_train, X_test, y_train, y_test = \
                train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
        dim = X_train.shape[1]
        self.indices_ = tuple(range(dim))
        self.subsets_ = [self.indices_]
        score = self._calc_score(X_train, y_train, X_test, y_test, self.indices_)
        #get score
        self.scores_ = [score]
        # iterate untill it reahes k_ffeatres
        while dim > self.k_features:
            #initialize list  
            scores = []
            subsets = []

            for p in combinations(self.indices_, r=dim - 1):
                #store score
                #try all pattern
                score = self._calc_score(X_train, y_train, X_test, y_test, p)
                scores.append(score)
                subsets.append(p)
           
            #get maxindex
            best = np.argmax(scores)
            self.indices_ = subsets[best]
            self.subsets_.append(self.indices_)
            dim -= 1
            self.scores_.append(scores[best])

        self.k_score_ = self.scores_[-1]
        return self

    def transform(self, X):
        return X[:, self.indices_]

    def _calc_score(self, X_train, y_train, X_test, y_test, indices):
        self.estimator.fit(X_train[:, indices], y_train)
        y_pred = self.estimator.predict(X_test[:, indices])
        score = self.scoring(y_test, y_pred)
        return score

if(__name__ == '__main__'):
    from sklearn.neighbors import KNeighborsClassifier
    import matplotlib.pyplot as plt
    knn = KNeighborsClassifier(n_neghbors=5)
    sbs = SBS(knn, k_features=1)
    sbs.fit(X_train_std, y_train)








