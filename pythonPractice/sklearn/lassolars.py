from sklearn.linear_model import LassoLarsCV
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
X, y = make_regression(n_features=1, noise=4.0, random_state=0)
y = y.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100)
reg = LassoLarsCV(cv=5).fit(X_train, y_train)
print(reg.score(X_train, y_train))
print(reg.score(X_test, y_test))
print(reg.alpha_)
y_pred = reg.predict(X)
print(X_train.shape, y_train.shape)
plt.scatter(X_train, y_train, label='train')
plt.scatter(X_test, y_test, label='test')
plt.plot(X, y_pred)
plt.show()


