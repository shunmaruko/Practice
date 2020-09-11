from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)
X, y = make_regression(n_samples=1000, random_state=1)
print(X.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
sc = StandardScaler()
sc.fit(X_train)
X_train_std, X_test_std = sc.transform(X_train), sc.transform(X_test)
hidden = [(80,60,40,20,10), (120,100,80,60,20)] 
parameters = {'hidden_layer_sizes':hidden, 'max_iter':(3000,), 'early_stopping':(True,)}
#regr = MLPRegressor(random_state=1, batch_size=32, max_iter=3000, solver='adam', activation='relu', hidden_layer_sizes=(80,60,40,10)).fit(X_train_std, y_train)
regr_grid = GridSearchCV(MLPRegressor(), parameters, scoring='neg_mean_squared_error', n_jobs=-1)
regr_grid.fit(X_train_std, y_train)
y_train_pred = regr_grid.predict(X_train_std)
y_test_pred = regr_grid.predict(X_test_std)
print("Best scpre",regr_grid.best_score_)
print("Best parameters",regr_grid.best_params_)
print("Determination R^2 train:", regr_grid.score(X_train_std, y_train))
print("Determination R^2 test :", regr_grid.score(X_test_std, y_test))
print("MSE train", mean_squared_error(y_train_pred, y_train))
print("MSE test ", mean_squared_error(y_test_pred, y_test))


