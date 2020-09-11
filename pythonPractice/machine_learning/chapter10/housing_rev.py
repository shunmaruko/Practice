from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
boston = load_boston()
X = boston.data[:, 12].reshape(-1, 1) 
y = boston.target.reshape(-1, 1)
regr = LinearRegression()
X_log = np.log(X)
X_fit = np.arange(X_log.min()-1, X_log.max()+1, 1).reshape(-1, 1)
regr = regr.fit(X_log, y)
y_lin_fit = regr.predict(X_fit)
linear_r2 = r2_score(y, regr.predict(X_log))

plt.scatter(X_log, y, label='traininig points', color='lightgray')
plt.plot(X_fit, y_lin_fit, label='linear $R^2=%.2f$' % linear_r2, color='blue')
plt.xlabel('log(lower status of the population [LSTAT])')
plt.ylabel('Price in $1000s [MEDV]')
plt.legend(loc='upper right')
plt.show()
