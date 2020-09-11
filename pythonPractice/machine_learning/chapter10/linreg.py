from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def lin_regplot(X, y, model):
    plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
    plt.plot(X, model.predict(X), color='black', lw=2)
    return
if (__name__=='__main__'):
    boston = load_boston()
    #extract 'RM'
    X = boston.data[:,5].reshape(-1,1)
    y = boston.target.reshape(-1,1)
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    X_std, y_std = sc_x.fit_transform(X), sc_y.fit_transform(y).flatten()
    print(X_std.shape, y_std.shape)
    slr = LinearRegression()
    slr.fit(X, y)
    y_pred = slr.predict(X)
    print('Slope : {}'.format(slr.coef_[0]))
    print('Intercept : {}'.format(slr.intercept_))
    lin_regplot(X, y, slr)
    plt.xlabel('Average number of RM')
    plt.ylabel('Price in $1000s [MEDV]')
    plt.show()
