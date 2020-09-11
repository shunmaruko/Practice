from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from firststep import plot_decision_regions

#preprocess
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
print('Class labels: {}'.format(np.unique(y)))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
#standalization
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

#create instance of logittic regression
lr_clf = LogisticRegression(C=100.0, random_state=1)
#C: float
# Inverse of regularization strength 
lr_clf.fit(X_train_std, y_train)

#plot decision boundary
plot_decision_regions(X=X_combined_std, y=y_combined, classifier=lr_clf, test_idx=range(105, 150))
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()
print("probability of belonging to class 0 1 2")
print(lr_clf.predict_proba(X_test_std[:3,:]).argmax(axis=1))
print(lr_clf.predict(X_test_std[:3, :]))
#sklearn expect to input 2-D array, so if input 1-d array 
#we need to convert [sample] to [[sample]] using reshape(1, -1)
print(lr_clf.predict(X_test_std[0, :]).reshape(1, -1))
