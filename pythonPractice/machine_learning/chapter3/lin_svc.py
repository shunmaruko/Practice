from sklearn.svm import SVC
#preprocess
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#plotter
from firststep import plot_decision_regions
import numpy as np
import matplotlib.pyplot as plt

#arrange datasets
iris = datasets.load_iris()
X = iris.data[:,[2,3]]
y = iris.target
print(X.shape)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

#make insrtance of linear SVC
svm = SVC(kernel='linear', C=0.1, random_state=1)
"""
Parameters
----------
C : float
  regularization parameter
"""
svm.fit(X_train_std, y_train)
plot_decision_regions(X_combined_std, y_combined, classifier=svm, test_idx=range(105,150))
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

