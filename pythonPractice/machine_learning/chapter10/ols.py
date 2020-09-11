from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class LinearRegressionGD(object):
    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)


def lin_regplot(X, y, model):
    plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
    plt.plot(X, model.predict(X), color='black', lw=2)
    return

if (__name__ == "__main__"):
    boston = load_boston()
    #extract 'RM'
    X = boston.data[:,5]
    y = boston.target
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    X_std, y_std = sc_x.fit_transform(X.reshape(-1,1)), sc_y.fit_transform(y.reshape(-1,1)).flatten()
    print(X_std.shape, y_std.shape)
    lr = LinearRegressionGD()
    lr.fit(X_std, y_std)
    plt.plot(range(1, lr.n_iter+1), lr.cost_)
    plt.ylabel('SSE')
    plt.xlabel('Epoch')
    plt.show()

    lin_regplot(X_std, y_std, lr)
    plt.xlabel('Average number of rooms [RM] (standardized)')
    plt.ylabel('Price in $1000s [MEDV] (standardized)')
    plt.show()
    #predict price in case of 5 rooms
    num_rooms_std = sc_x.transform([[5.0]])
    print(num_rooms_std.shape)
    price_std = lr.predict(num_rooms_std)
    print('Prince in $1000s : {}'.format(sc_y.inverse_transform(price_std)))


