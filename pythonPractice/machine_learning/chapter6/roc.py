from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.model_selection import StratifiedKFold
import matplotlib as mp
mp.rcParams['font.family'] = 'Times New Roman'
mp.rcParams['lines.linewidth'] = 2 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

df = pd.read_csv('~/Downloads/wdbc.data', header=None)
X, y = df.iloc[:,2:].values, df.iloc[:,1].values
print(X[y == 'M'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=1)
X_train2 = X_train[:,[4, 14]]
pipe_lr = make_pipeline(StandardScaler(),
                        PCA(n_components=2),
                        LogisticRegression(penalty='l2', random_state=1, C=100.0))
cv = list(StratifiedKFold(n_splits=3, random_state=1).split(X_train, y_train))
fig = plt.figure(figsize=(7, 5))
mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)
all_tpr = []

