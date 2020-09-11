import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import perceptron as pc
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, resolution=0.02):
    #arrange color map and marker 
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    #in this case len(y) = 2
    cmap = ListedColormap(colors[:len(np.unique(y))])

    #plot decision boundary
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    #1-D dimension and transpose 
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    #convert data 
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    #lim of each axis
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    #plot sample data 
    for idx, cl in enumerate(np.unique(y)):
        """
        boolean index
        extract data by boolean index
        e,g a = np.array([0,1,2])
        bind = [True, False, False]
        a[bind] 
        >> [0]
        """
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx], 
                    marker=markers[idx], 
                    label=cl,
                    edgecolor='black')
if (__name__ == "__main__"):
    """Iris datasets"""
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
    df.tail()
    #extract objective varibales from 1 to 100
    y = df.iloc[0:100, 4].values
    #convert label to int
    y = np.where(y == 'Iris-setosa', -1, 1)
    #iloc designate 
    x = df.iloc[0:100, [0, 2]].values
    plt.scatter(x[:50,0], x[:50,1], color='red', marker='o', label='setosa')
    plt.scatter(x[50:100,0], x[50:100,1], color='blue', marker='x', label='versicolor')
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()
    plt.clf()
    #make instance
    ppn = pc.Perceptron(eta=0.01,n_iter=10)
    ppn.fit(x,y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of updates')
    plt.show()
    plt.clf()
    
    plot_decision_regions(x, y, classifier=ppn)
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()
