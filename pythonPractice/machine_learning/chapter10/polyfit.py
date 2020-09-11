from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = np.array([258., 270., 294., 320., 342., 368., 396., 446., 480., 586.]).reshape(-1, 1)
y = np.array([236.4, 234.4, 252.8, 298.6, 314.2, 342.2, 360.8, 368.0, 391.2, 390.8])
X_fit = np.arange(250, 600, 10).reshape(-1, 1)

lr = LinearRegression()
lr.fit(X, y)
y_lin_fit = lr.predict(X_fit)

quadratic = PolynomialFeatures(degree=2)
X_quad = quadratic.fit_transform(X)
pr = LinearRegression()
pr.fit(X_quad, y)
y_quad_fit = pr.predict(quadratic.fit_transform(X_fit))
plt.scatter(X, y, label='training points')
plt.plot(X_fit, y_lin_fit, label='linear fit', linestyle='--')
plt.plot(X_fit, y_quad_fit, label='quadratic fit')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

y_lin_pred = lr.predict(X)
y_quad_pred = pr.predict(quadratic.fit_transform(X))
print('MSE lin: %e poly: %e' % (mean_squared_error(y, y_lin_pred),
                                  mean_squared_error(y, y_quad_pred)))
print("R^2 lin: %e poly: %e" % (r2_score(y, y_lin_pred),
                                  r2_score(y, y_quad_pred)))
