from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

boston = load_boston()
X = boston.data[:,:]
y = boston.target.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
slr = LinearRegression()
slr.fit(X_train, y_train)
y_train_pred = slr.predict(X_train)
y_test_pred = slr.predict(X_test)
#residual plot
plt.scatter(y_train_pred, y_train_pred - y_train, 
            c='steelblue', marker='o', edgecolor='white', label='Training data')
plt.scatter(y_test_pred, y_test_pred - y_test, 
            c='limegreen', marker='s', edgecolor='white', label='Test data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=-10, xmax=50, color='black', lw=2)
plt.xlim([-10, 50])
plt.tight_layout()
plt.show()
#mean squared error
print('MSE train: %e test: %e' % (mean_squared_error(y_train, y_train_pred),
                                  mean_squared_error(y_test, y_test_pred)))
print("R^2 train: %e test: %e" % (r2_score(y_train, y_train_pred),
                                     r2_score(y_test, y_test_pred)))

