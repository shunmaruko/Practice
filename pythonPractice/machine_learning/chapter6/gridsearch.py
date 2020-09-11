from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib as mp
mp.rcParams['font.family'] = 'Times New Roman'
mp.rcParams['lines.linewidth'] = 2 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

warnings.simplefilter("ignore")
#get data
df = pd.read_csv('~/Downloads/wdbc.data', header=None)
X, y = df.iloc[:,2:].values, df.iloc[:,1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=1)
pipe_svc = make_pipeline(StandardScaler(),
                         SVC(random_state=1))
param_range = [10**i for i in range(-3,4,1)]
param_grid = [{'svc__C': param_range, 'svc__kernel': ['linear']},
              {'svc__C': param_range, 'svc__gamma': param_range,
               'svc__kernel': ['rbf']}]
gs = GridSearchCV(estimator=pipe_svc,
                  param_grid=param_grid,
                  scoring='accuracy',
                  cv=10,
                  n_jobs=-1)
gs = gs.fit(X_train, y_train)
print(gs.best_score_)
print(gs.best_params_)
clf = gs.best_estimator_
clf.fit(X_train, y_train)
print('Test accuracy {}'.format(clf.score(X_test, y_test)))
