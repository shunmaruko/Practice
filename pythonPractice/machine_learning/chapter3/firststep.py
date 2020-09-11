from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    #prepare marker and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    #plot decision region
    x1_min, x1_max = X[:, 0].min() - 1, X[:,0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:,1].max() + 1
    #make mesh
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    #prediction
    Z = classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    #plot countour
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    # set axis range
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # sample plot
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[ y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')
    # bold test sample
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0],
                    X_test[:, 1],
                    c='',
                    edgecolor='black',
                    alpha=1.0,
                    linewidth=1,
                    marker='o',
                    s=100,
                    label='test set')

if (__name__ == "__main__"):
    iris = datasets.load_iris()
    print(iris.data[:,[2,3]])
    X = iris.data[:,[2,3]]
    #get class label
    y = iris.target
    print('Class labels:', np.unique(y))
    #label is already turned into integer
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
    print(X_test.shape, y_test.shape)
    #test size is propotion of datasize to train size
    #if random state is designated, we can reproduce this random order 
    #if stratify isn't None, the ratio of train data to test data become same
    print('Labels counts in y:', np.bincount(y))
    print('Labels counts in y_train:', np.bincount(y_train))
    print('Labels counts in y_test:', np.bincount(y_test))
    
    sc = StandardScaler()
    #calculate mean and deviation of traininig data
    sc.fit(X_train)
    print("sample variance",sc.var_,"sample mean",sc.mean_)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    #make instance of calssifier
    clf = Perceptron(max_iter=40, eta0=0.1, random_state=1)
    #training data
    clf.fit(X_train_std, y_train)
    #fit training data to model by SGD
    y_pred = clf.predict(X_test_std)
    print(help(Perceptron))
    print('Misclassified samples: %d' % (y_test != y_pred).sum())
    print('Total samples: %d' % len(y_test))
    print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
    
    #combine train and test data look like append
    #X : shape = (n_sample, n_features)
    X_combined_std = np.vstack((X_train_std, X_test_std))
    #combine trainning and test label
    #Y : shape = (n_sample,)
    #By default (n,) represents (1,2,....,n)
    y_combined = np.hstack((y_train, y_test))
    #plot
    firststep.plot_decision_regions(X=X_combined_std, y=y_combined, classifier=clf, test_idx=range(105,150))
    
    #setting of axis
    plt.xlabel('petal length [standalized]')
    plt.ylabel('petal width [standalized]')
    
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


