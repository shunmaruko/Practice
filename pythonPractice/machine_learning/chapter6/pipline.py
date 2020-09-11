import warnings
warnings.simplefilter("ignore")
import pandas as pd
#get data
df = pd.read_csv('~/Downloads/wdbc.data', header=None)
X, y = df.iloc[:,2:].values, df.iloc[:,1].values

#preprocessing
#label encoding
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
y = class_le.fit_transform(y)
print("check class labels",class_le.classes_, class_le.transform(class_le.classes_))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=1)
print("X_train",X_train)
print("X_test",X_test)

#make pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
pipe_lr = make_pipeline(StandardScaler(), 
                       PCA(n_components=2),
                       LogisticRegression(random_state=1))
pipe_lr.fit(X_train, y_train)
y_pred = pipe_lr.predict(X_test)
print('Test Accuracy: {}'.format(pipe_lr.score(X_test, y_test)))

#stratified k-fold cross validation
import numpy as np
from sklearn.model_selection import StratifiedKFold
"""1 way
kfold = StratifiedKFold(n_splits=10, random_state=1).split(X_train, y_train)
scores = []
for k, (train_index, test_index) in enumerate(kfold):
    print(X_train[[1]])
    pipe_lr.fit(X_train[train_index], y_train[train_index])
    score = pipe_lr.score(X_train[test_index], y_train[test_index])
    scores.append(score)
    print('Fold : {}, Class dist : {}, Acc : {}'.format(k+1, np.bincount(y_train[train_index]), score))

print('CV accuracy: {} +/- {}'.format(np.mean(scores), np.std(scores)))
"""
#another way
#whoooooo too simple and easy to use
from sklearn.model_selection import cross_val_score
scores = cross_val_score(estimator=pipe_lr, X=X_train, y=y_train, cv=10, n_jobs=-1)
print('CV accuracy scores:{}'.format(scores))
print('CV accuracy: {} +/- {}'.format(np.mean(scores), np.std(scores)))

