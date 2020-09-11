from sklearn.linear_model import RANSACRegressor 
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

boston = load_boston()
X = boston.data[:,5].reshape(-1,1)
y = boston.target.reshape(-1,1)
#print(X.shape, y.shape)

ransac = RANSACRegressor(LinearRegression(),
                         max_trials=100,
                         min_samples=50,
                         loss='absolute_loss',
                         residual_threshold=5.0,
                         random_state=0)
ransac.fit(X,y)
X = boston.data[:,5].reshape(-1,1)
y = boston.target.reshape(-1,1)
inlier_mask = ransac.inlier_mask_
#print(type(inlier_mask), inlier_mask.shape)
outlier_mask = np.logical_not(inlier_mask)
line_X = np.arange(3, 10 ,1)
line_y_ransac = ransac.predict(line_X.reshape(-1, 1))
plt.scatter(X[inlier_mask], y[inlier_mask], c='steelblue', edgecolor='white', marker='o', label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], c='limegreen', edgecolor='white', marker='s', label='Outliers')
plt.plot(line_X, line_y_ransac, color='black', lw=2)
plt.legend(loc='upper left')
plt.show()

