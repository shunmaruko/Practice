from matplotlib.dates import DateFormatter
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 
from sklearn.preprocessing import Imputer
from sbs import SBS 
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import seaborn as sns
import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
"""
read csv file
"""
files = glob.glob('./*csv')
df = pd.DataFrame()
for filename in files:
    df_temp = pd.read_csv(filename, header=1,encoding='cp932')
    print(filename, df_temp.shape)
    df = df.append(df_temp)
"""
preprocess
"""
df.columns.values[:] = ["date", "start price", "high price", "low price", "end price", "volume", "adjusted value"]
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d', errors='ignore')
df = df.sort_values(by='date')
print(df.head())
date_mapping = { date : idx for idx, date in enumerate(df['date'].values)}
df['date'] = df['date'].map(date_mapping)
print(df.info())
split_ratio = 0.75
split_index  = int(df.shape[0] * split_ratio)
price_train, date_train = df.iloc[1:split_index, 1:], df.iloc[1:split_index, 0]
price_test, date_test = df.iloc[split_index:, 1:], df.iloc[split_index:, 0]
returns_train = pd.Series(price_train["end price"].values).pct_change().values
returns_test = pd.Series(price_test["end price"].values).pct_change().values
imr_train = Imputer(missing_values='NaN', strategy='mean', axis=0)
imr_test = Imputer(missing_values='NaN', strategy='mean', axis=0)
imr_train = imr_train.fit(returns_train.reshape(-1,1))
imr_test = imr_test.fit(returns_test.reshape(-1,1))
returns_train = imr_train.transform(returns_train.reshape(-1,1)).flatten()
returns_test = imr_test.transform(returns_test.reshape(-1,1)).flatten()
"""
feature extraction
"""
n_days = 5 
def make_dataset(price, n_features):
    train_X = []
    train_y = []
    for now in range(n_features, len(price)):
        start = now - n_features
        train_X.append(price[start:now])
        train_y.append(price[now])
    return np.array(train_X), np.array(train_y)

X_train, y_train = make_dataset(returns_train, n_features=n_days)
X_test, y_test = make_dataset(returns_test, n_features=n_days)
print('shape of train data', X_train.shape, y_train.shape)
"""
plot data
"""
average25_price = df["end price"].rolling(window=25, center=False,  axis=0).agg(['mean'])
average50_price = df["end price"].rolling(window=50, center=False,  axis=0).agg(['mean'])
#plt.plot(date.values, price['end price'].values,  color="limegreen", label='end price')
#plt.plot(date.values.reshape(-1,1), average25_price[:-1],  color="lightpink", label='25 average price')
#plt.plot(date.values.reshape(-1,1), average50_price[:-1],  color="lightcoral", label='50 average price')
print(price_train.shape)
plt.plot(date_train, price_train['end price'].values, color='lightpink', label="train data")
plt.plot(date_test, price_test['end price'].values, color='limegreen', label="test data")
plt.ylim(0,5000)
plt.legend()
plt.show()
"""feature selection 
Sequential Backward Selection method with 5 nearest neighbors model 
"""
scaler_x = StandardScaler()
scaler_y = StandardScaler()
X_train_std, y_train_std = X_train, y_train
X_test_std, y_test_std = X_test, y_test
df_data = pd.DataFrame(X_train_std)
df_data.columns.value = list(range(n_days))
sns.pairplot(df_data, size=1.0)
#plt.xlabel('Number of features')
#plt.ylabel('Accuracy')
#plt.grid()
#plt.tight_layout()
#plt.show()
"""
train algorithm 
"""
regr = RandomForestRegressor(n_estimators=10000,
                             criterion='mse',
                             random_state=1,
                             n_jobs=-1)
print(regr.max_depth)
regr.fit(X_train_std, y_train)
y_train_pred = regr.predict(X_train_std)
y_test_pred = regr.predict(X_test_std)
print("train mse", mean_squared_error(y_train, y_train_pred))
print("test  mse", mean_squared_error(y_test, y_test_pred))
y_test_pred[0:n_days] = price_test['end price'].values[0:n_days]
y_train_pred[0:n_days] = price_train['end price'].values[0:n_days]
price_test_pred = [y_test_pred[i] for i in range(n_days)]
price_train_pred = [y_train_pred[i] for i in range(n_days)]
for i in range(n_days, y_test_pred.shape[0]):
    price_dum  = y_test_pred[i-1] * (1.0 + y_test_pred[i])
    y_test_pred[i] = price_dum
    price_test_pred.append(price_dum)
for i in range(n_days, y_train_pred.shape[0]):
    price_dum  = y_train_pred[i-1] * (1.0 + y_train_pred[i])
    y_train_pred[i] = price_dum
    price_train_pred.append(price_dum)

plt.clf()
plt.plot(np.arange(len(price_test_pred)), price_test_pred, label="predicted")
plt.plot(np.arange(len(price_test_pred)+n_days), price_test["end price"].values, label="test")
plt.ylim(0,5000)
plt.legend()
plt.tight_layout()
plt.show()

plt.clf()
plt.plot(np.arange(len(price_train_pred)), price_train_pred, label="predicted")
plt.plot(np.arange(len(price_train_pred)+n_days), price_train["end price"].values, label="train")
plt.ylim(0,5000)
plt.tight_layout()
plt.legend()
plt.show()
