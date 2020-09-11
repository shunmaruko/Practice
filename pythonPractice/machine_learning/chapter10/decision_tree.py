from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from linreg import lin_regplot 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
boston = load_boston()
X = boston.data[:, 12].reshape(-1, 1) 
y = boston.target.reshape(-1, 1)
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X, y)
sort_idx = X.flatten().argsort()
lin_regplot(X[sort_idx], y[sort_idx], tree)
plt.xlabel('lower status of the population [LSTAT]')
plt.ylabel('Price in $1000s [MEDV]')
plt.show()

