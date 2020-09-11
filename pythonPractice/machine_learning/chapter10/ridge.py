from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

boston = load_boston()
X = boston.data[:,:]
y = boston.target.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=1.0)
elanet = ElasticNet(alpha=1.0, l1_ratio=0.5)
ridge.fit(X_train, y_train)
y_test_pred = ridge.predict(X_test)
print(y_test_pred.shape, y_test.shape)
plt.scatter(y_test_pred, y_test_pred - y_test, c='limegreen', label='ridge')
lasso.fit(X_train, y_train)
y_test_pred = lasso.predict(X_test).reshape(-1, 1)
print(y_test_pred.shape, y_test.shape)
plt.scatter(y_test_pred, y_test_pred - y_test, c='lightcoral', label='lasso')
elanet.fit(X_train, y_train)
print(y_test_pred.shape, y_test.shape)
y_test_pred_3  = elanet.predict(X_test).reshape(-1, 1)
plt.scatter(y_test_pred, y_test_pred - y_test, c='lightpink', label='elanet')
plt.legend(loc='best')
plt.tight_layout()
plt.show()


