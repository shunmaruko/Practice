import matplotlib.pyplot as plt
import numpy as np

#set random seed
np.random.seed(1)
#shape(200, 2)
X_xor = np.random.randn(200,2) 
y_xor = np.logical_xor(X_xor[:,0] > 0, X_xor[:,1] > 0)
#True -> 1, False -> -1
y_xor = np.where(y_xor, 1, -1)
"""
XOR gate
A B A xor B
L L L
L H H
H L H
H H L
"""
plt.scatter(X_xor[y_xor==1,0], X_xor[y_xor==1, 1],
            c='b', marker='x', label='1')

plt.scatter(X_xor[y_xor==-1,0], X_xor[y_xor==-1, 1],
            c='r', marker='s', label='-1')
plt.xlim([-3,3])
plt.ylim([-3,3])
plt.legend(loc='best')
plt.tight_layout()
plt.show()

from sklearn.svm import SVC
#Radial Basis Funvtion kernel
svm = SVC(kernel='rbf', random_state=1, gamma=100, C=10.0)
svm.fit(X_xor, y_xor)
from firststep import plot_decision_regions
plot_decision_regions(X_xor, y_xor, classifier=svm)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
