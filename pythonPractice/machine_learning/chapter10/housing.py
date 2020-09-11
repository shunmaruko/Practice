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
#y = df['MEDV'].values
quadratic = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
X_quad = quadratic.fit_transform(X)
X_cubic = cubic.fit_transform(X)

X_fit = np.arange(X.min(), X.max(), 1).reshape(-1, 1)
regr = regr.fit(X, y)
y_lin_fit = regr.predict(X_fit)
linear_r2 = r2_score(y, regr.predict(X))

regr = regr.fit(X_quad, y)
y_quad_fit = regr.predict(quadratic.fit_transform(X_fit))
quadratic_r2 = r2_score(y, regr.predict(X_quad))

regr = regr.fit(X_cubic, y)
y_cubic_fit = regr.predict(cubic.fit_transform(X_fit)) 
cubic_r2 = r2_score(y, regr.predict(X_cubic))

plt.scatter(X, y, label='traininig points', color='lightgray')
plt.plot(X_fit, y_lin_fit, label='linear $R^2=%.2f$' % linear_r2, color='blue')
plt.plot(X_fit, y_quad_fit, label='quad $R^2=%.2f$' % quadratic_r2, color='red')
plt.plot(X_fit, y_cubic_fit, label='quad $R^2=%.2f$' % cubic_r2, color='green')
plt.xlabel('lower status of the population [LSTAT]')
plt.ylabel('Price in $1000s [MEDV]')
plt.legend(loc='upper right')
plt.show()
