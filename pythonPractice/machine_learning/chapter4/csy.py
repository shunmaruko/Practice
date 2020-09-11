import pandas as pd
from io import StringIO
from sklearn.preprocessing import Imputer

csv_data='''A,B,C,D
            1.0,2.0,3.0,4.0
            5.0,6.0,,8.0
            10.0,11.0,12.0,'''
#resd(filename or StringIO object
df = pd.read_csv(StringIO(csv_data))
print(df)
print(df.values)
print(df.isnull())
print(df.isnull().sum())
#delete raw icluding NaN
print(df.dropna(axis=0))
#delete colum icluding NaN
print(df.dropna(axis=1))
#delete raw if all values are NaN
print(df.dropna(how='all'))
#de;te raw if number of values is less than 4
print(df.dropna(thresh=4))
#mean imputation
imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
imr = imr.fit(df.values)
#execute interpolation
imputed_data = imr.transform(df.values)
print(imputed_data)
