import numpy as np

class LogisticRegressionGD():
    """Logistic Regression with gradient descent classifier

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
    cost_ : list
        number of updates per epoch
    """
    def __init__(self, eta=0.01, n_iter=50, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        self.shuffle = shuffle
        self.w_initialized = False

    def _shuffle(self, X, y):
        """
        shuffle training data
        """
        #randomly select index 
        r = self.rgen.permutation(len(y))
        return X[r], y[r]

    def _update_weights(self, xi, target):
        output = self.activation(self.net_input(xi))
        error = target - output
        self.w_[1:] += self.eta * xi.T.dot(error)
        self.w_[0] += self.eta * error
        #for most likelihood function
        cost = (error**2)/2.
        return cost 
        

        
    def _initialize_weight(self,m):
        """
        initialize w_

        Parameters
        ----------
        m : int
            size of w_
        """
        if not self.w_initialized:
            self.rgen = np.random.RandomState(seed=self.random_state)
            #loc : mean, scale : standard deviation
            #under bar after variable is used to avoid collision of python keywords
            self.w_ = self.rgen.normal(loc=0., scale=0.01, size=1+m)
            self.w_initialized = True


    def fit(self, X, y):
        """Fit to training data

        Parameters
        ----------
        X : array_like, shape = {n_samples, n_features}
            training data
        y : array_like, shape = (n_samples,)
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
        #rgen = np.random.RandomState(seed=self.random_state)
        #loc : mean, scale : standard deviation
        #under bar after variable is used to avoid collision of python keywords
        self._initialize_weight(X.shape[1])
        self.cost_ = []
        for _ in range(self.n_iter):
            costs = 0
            # z = x_i*w_i, shape = (n_samples,)
            if self.shuffle:
                X, y = self._shuffle(X,y)
            net_input = self.net_input(X)
            cost = []
            #for xi, yi in zip(X, y):
            #    cost.append(self._update_weights(xi, yi))
            #avg_cost = sum(cost)/len(cost)
            #self.cost_.append(avg_cost)
            #act(z)
            output = self.activation(net_input)
            errors =  y - output
            print(errors)
            #dwj := eta * error^i * x^i_j, shape = 
            ##errors are borad casted
            ## (2, 100) * (100,) -> (2,)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            costs = -y.dot(np.log(output)) - ((1- y).dot(np.log(1-output)))
            self.cost_.append(costs)
        return self
    
    def net_input(self, X):
        """ 
        calculate total input
       
        weights are broadcasted implicitly
        """
        return np.dot(X,self.w_[1:]) + self.w_[0]

    def activation(self, z):
        return self.sigmoid(z) 

    def sigmoid(self,z):
        return 1.0/(1.0 + np.exp(-z))

    def predict(self, X):
        """return class label
        if predict is more than 0, returns 1
        otherwise, returns -1
        """
        return np.where(self.net_input(X) >= 0.0, 1, 0)

if (__name__ == "__main__"):
    import pandas as pd
    import matplotlib.pyplot as plt
    import sys
    sys.path.append("../chapter2/")
    import iris
    """Iris datasets"""
    #preprocess
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
    df.tail()
    #extract objective varibales from 1 to 100
    y = df.iloc[0:100, 4].values
    #convert label to int
    #for logidstic classification
    y = np.where(y == 'Iris-setosa', 0, 1)
    print(y)
    #iloc designate 
    x = df.iloc[0:100, [0, 2]].values
    # deep copy x
    x_std = np.copy(x)
    #standalization
    x_std[:,0] = (x_std[:,0] - x_std[:,0].mean())/x_std[:,0].std()
    x_std[:,1] = (x_std[:,1] - x_std[:,1].mean())/x_std[:,1].std()

    #Training
    clf = LogisticRegressionGD(n_iter=100, eta=0.01, random_state=1).fit(x_std,y)
    iris.plot_decision_regions(x_std,y,classifier=clf)
    plt.title('AdalineGD')
    plt.xlabel('sepal length standarlized')
    plt.ylabel('petal length standarlized')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

    plt.plot(range(1,len(clf.cost_)+1),clf.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Sum Squeared Error')
    plt.tight_layout()
    plt.show()

"""
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    ada1 = Adaline(n_iter=10, eta=0.01).fit(x,y)
    ax[0].plot(range(1,len(ada1.cost_)+1),np.log10(ada1.cost_), marker='o')
    ax[0].set_xlabel('Epochs')
    ax[0].set_ylabel('Log10(Sum Squeared Error)')
    ax[0].set_title('Adaline - lr 0.01')

    ada2 = Adaline(n_iter=10, eta=0.0001).fit(x,y)
    ax[1].plot(range(1,len(ada2.cost_)+1),ada2.cost_, marker='o')
    ax[1].set_xlabel('Epochs')
    ax[1].set_ylabel('Sum Squeared Error')
    ax[1].set_title('Adaline - lr 0.0001')
    plt.show()
"""
