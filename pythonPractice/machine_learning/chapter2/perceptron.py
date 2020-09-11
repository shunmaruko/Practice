import numpy as np
class Perceptron():
    """Clustering Perceptron

    Parameters
    ----------
    eta : float
        learning rate
    n_iter : int 
        number of iteration
    random_state : int
        random seed to initialize weights

    Attributes
    ---------
    w_ : ndarray 
        1D array containing data with 'float' type. 
        shape = n_features + 1 (bias unit)
        represents weight
    errors : list
        number of updates per epoach
    """
    def __init__(self,eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """Fit to training data

        Parameters
        ----------
        X : array_like, shape = {n_samples, n_features}
            training data
        y : array_like, shape = [n_samples]
            objective variable

        Returns
        -------
        self : object
            if return self, we can use method chain
        """
        """
        generate a random number is generated called The Mersenne Twister is a pseudorandom number generator (PRNG) 
        The benefit is it can set random seed and helpful for 
        debuggin or check the parallel computing it has multiple random streams
        """
        rgen = np.random.RandomState(seed=self.random_state)
        #loc : mean, scale : standard deviation
        #under bar after variable is used to avoid collision of python keywords
        self.w_ = rgen.normal(loc=0., scale=0.01, size=1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for Xi, target in zip(X,y):
                #update weights
                #dw_j := eta(y^i-\bar{y^i})x^i_j for j=1...n_features
                update = self.eta * (target -self.predict(Xi))
                self.w_[1:] += update * Xi
                #update w0
                #dw0 = eta(y^i - \bar{y^i}) * 1.0
                self.w_[0] += update * 1. 
                #True equals to 1, as bool is sub class of int
                errors += int(update != 0.) 
            self.errors_.append(errors)
        return self
    
    def net_input(self,X):
        """ calculate total input"""
        return np.dot(X,self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """return class label
        if predict is more than 0, returns 1
        otherwise, returns -1
        """
        return np.where(self.net_input(X) >= 0.0, 1, -1)

if (__name__ == "__main__"):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
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
    ppn = Perceptron(eta=0.01,n_iter=10)
    ppn.fit(x,y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of updates')
    plt.show()


