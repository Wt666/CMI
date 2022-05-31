import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import TweedieRegressor

url = "C:/Users/rexwang/Downloads/train.csv"
df = pd.read_csv(url, header=None)
# print(df[:,-1])
data = df.values
# print(data[:,-1])
X, y = data[:, :-1], data[:, -1] # 获取X为第1列到n-1列，y是最后一列(Result)
# print(X)
# print(X.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # train data from train.csv
# print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# define model
model = KNeighborsRegressor()  # can choose other algorithms
model.fit(X_train, y_train)  # fit model
# make predictions
ypredict = model.predict(X_test)
# evaluate predictions
mae = mean_absolute_error(y_test, ypredict)  # accuracy
print('MAE: %.5f' % mae)

url2 = "C:/Users/rexwang/Downloads/test.csv"
df2 = pd.read_csv(url2, header=None)
data2 = df2.values
# print(data2)
X_PRE = data2[:]
model.fit(X, y)
# print(X_PRE.shape)
Y_PRE = model.predict(X_PRE)  # Predict Testing data
df2[''] = Y_PRE
df2.to_csv(r"C:/Users/rexwang/Downloads/test.csv", mode='w', index=False, header=None)  # Import
data3 = df2.values
# print(data3)
print('=== Predict result to_csv ===, done.')
