import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_wine = pd.read_csv("~/Downloads/wine.data", header=None)
df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
                   'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
print('Class labels' , np.unique(df_wine['Class label']))
print(df_wine.head())
print(df_wine.iloc[:,1])
#split characteristic and class label
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:,0].values
#split data into training data and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
#normalization
from sklearn.preprocessing import MinMaxScaler
#make instance of min-max scaling
mms = MinMaxScaler()
#scaling trainnig data
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)

#standarization
from sklearn.preprocessing import StandardScaler
#make insitance
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

from sklearn.linear_model import LogisticRegression
#Logistic Regression with L1 norm
#inverse normalization parameter
lr = LogisticRegression(penalty='l1', C=1.0)
lr.fit(X_train_std, y_train)
print('Training accuracy:', lr.score(X_train_std, y_train))
print('Test accuracy:', lr.score(X_test_std, y_test))
print('w0 means intercept in sklearn')
print(lr.intercept_)
print('check all coefficient to select characteristc')
print(lr.coef_)
#visualization
n_class_label = len(np.unique(df_wine['Class label']))
fig, ax = plt.subplots(n_class_label,1)
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'pink',
          'lightgreen', 'lightblue', 'lightblue', 'gray', 'indigo', 'orange']
weights, params = [[] for i in range(n_class_label)], [[] for i in range(n_class_label)]
#try various inverse regualariatino parameter
for c in np.arange(-4., 6.):
    lr = LogisticRegression(penalty='l1', C=10.**c, random_state=1)
    lr.fit(X_train_std, y_train)
    for i_class_label in range(n_class_label):
        weights[i_class_label].append(lr.coef_[i_class_label])
        params[i_class_label].append(10**c)

#covert list to np.array
weights = np.array(weights)
for column, color in zip(range(weights.shape[2]),colors):
    for i_class_label in range(n_class_label):
        ax[i_class_label].plot(params[i_class_label], weights[i_class_label,:, column], label=df_wine.columns[column+1], color=color)
        
for i in range(n_class_label):
    ax[i].set_xlim([10**-5, 10**5])
    ax[i].set_xlabel('C')
    ax[i].set_ylabel('weight coefficient')
    ax[i].set_xscale('log')
    ax[i].grid(True)

plt.legend(loc='best')
#ax[:.1].legend(loc='upper right', bbox_to_anchor=(1.38, 1.03), ncol=1, fancybox=True)
#plt.tight_layout()
plt.show()
plt.clf()


#feature extraction by sequential backword selection
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from  sbs import SBS 
knn = KNeighborsClassifier(n_neighbors=5)
sbs = SBS(knn, k_features=1)
sbs.fit(X_train_std, y_train)
k_feat = [len(k) for k in sbs.subsets_]
print(df_wine.head())
print(" ")
k3 = list(sbs.subsets_[10])
print(df_wine.columns[1:][k3])
plt.plot(k_feat, sbs.scores_, marker='o')
plt.ylim([0.7, 1.02])
plt.ylabel('Accuracy')
plt.xlabel('Number of features')
plt.grid()
plt.tight_layout()
plt.show()

knn.fit(X_train_std, y_train)
print('Training accuracy:', knn.score(X_train_std, y_train))
print('Test accuracy:', knn.score(X_test_std, y_test))
knn.fit(X_train_std[:,k3], y_train)
print('Training accuracy:', knn.score(X_train_std[:,k3], y_train))
print('Test accuracy:', knn.score(X_test_std[:,k3], y_test))

from sklearn.ensemble import RandomForestClassifier
feat_labels = df_wine.columns[1:]
forest = RandomForestClassifier(n_estimators=500, random_state=1)
forest.fit(X_train, y_train)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
print(indices)

for f in range(X_train.shape[1]):
    print("{}) {}   {}".format(f, feat_labels[indices[f]], importances[indices[f]]))

plt.clf()
plt.title('Feature Importances')
plt.bar(range(X_train.shape[1]), importances[indices], align='center')
plt.xticks(range(X_train.shape[1]), feat_labels[indices], rotation=90)
plt.tight_layout()
plt.show()


