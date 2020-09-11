import pandas as pd
import numpy as np

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']
    ])
#set colum name
df.columns = ['color','size', 'price', 'classlabel'] 

#mappign of ordinal characteristics 
size_mapping = {'XL': 3, 'L': 2, 'M': 1}
inv_size_mapping = {v: k for k, v in size_mapping.items()}
df['size'] = df['size'].map(size_mapping)

#mappign of nominal characteristics 
#1method
#class -> number
class_mapping = {label:idx for idx, label in enumerate(np.unique(df['classlabel']))}
inv_class_mapping = {v: k for k, v in class_mapping.items()}
df['classlabel'] = df['classlabel'].map(class_mapping)
print(df)
df['classlabel'] = df['classlabel'].map(inv_class_mapping)
print(df)
#2method
from sklearn.preprocessing import LabelEncoder
#make instance of label encoder
class_le = LabelEncoder()
#convert classlabel ro integer
#fit + transform
y = class_le.fit_transform(df['classlabel'].values)
print(df)
print(y)
#extract color size price
X = df[['color', 'size', 'price']].values
color_le = LabelEncoder()
#covert color label to integer
X[:, 0] = color_le.fit_transform(X[:, 0])
print(X)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0], sparse=True)
print(ohe.fit_transform(X))
print(ohe.fit_transform(X).toarray())
#automataically calculate one hot vector
print(pd.get_dummies(df[['price', 'color', 'size']]))
#escape from multicolinearlity
print(pd.get_dummies(df[['price', 'color', 'size']], drop_first=True))

