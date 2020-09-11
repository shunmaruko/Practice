from sklearn.base import BaseEstimator
from sklearn.base import ClassifierMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import six
from sklearn.base import clone
from sklearn.pipeline import _name_estimators
import numpy as np
import operator

class MajorityVoteClassifier(BaseEstimator, ClassifierMixin):
    """Majority ensemble classifier

    Parameters
    ----------
    classifiers : array-like, shape =  [n_classfiers] 
        varisous classifiers

    vote : str, {'classlabel', 'probability'}, default = 'classlabel'
        'classlabel' -> prediction is based on argmax of classlabel
        'probability'-> prediction is based on argmax of probability

    weights : array-like, shape = [n_classifiers] (optional, defalut = None)
    """

    def __init__(self, classifiers, vote='classlabel', weights=None):
        self.classifiers = classifiers
        self.named_classifiers = {key: value for key, value in _name_estimators(classifiers)}
        self.vote = vote
        self.weights = weights

    def fit(self, X, y):
        """Train classifier

        Parameters
        ----------
        X : array-like, sparse matrix , shape = [n_samples, n_features]

        y : array-like, shape = [n_samples]

        Returns
        -------
        self : object

        """
        self.lablenc_ = LabelEncoder()
        self.labelenc_.fit(y)
        self.classes_ = seld.labelenc_.classes_
        self.classifiers_ = []
        for clf in self.classifiers:
            fitted_clf = clone(clf).fit(X, self.labelenc_.transform(y))
            self.classifiers_.append(fitted_clf)

        return self
    
    def predict(self, X):
        """predict class label of X

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]

        Returns
        -------
        maj_vote : array-like, shape = [n_samples]
            predicted class label
        """
        if self.vote == 'probability':
            maj_vote = np.argmax(self.predict_proba(X), axis=1)
        Returns
        -------
        avg_proba : array-like, shape = [n_samples, n_features]
            average of probabilities for each sample
        """
