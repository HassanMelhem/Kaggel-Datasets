# -*- coding: utf-8 -*-
"""House Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1udx258njEQWJiPBReZ6UYo3QlH4DuUQy

##Importing The Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""##Importing the California Housing Dataset"""

housing_price_dataset = sklearn.datasets.fetch_california_housing()
print(housing_price_dataset)

#loading the dataset into pandas dataframe
dataset = pd.DataFrame(housing_price_dataset.data, columns=housing_price_dataset.feature_names)
dataset

#adding the target column
dataset["Price"] = housing_price_dataset.target

dataset.head()

dataset.shape

#Check for missing values
dataset.isnull().sum()

#statistical measures on the data
dataset.describe()

"""## Understanding Correlation btw the Dataset features"""

correlation = dataset.corr()

#constructiong Heat Map to understand Correlation
plt.figure(figsize=(10, 10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, cmap="Blues")

"""##Splitting the data in features X and Target label"""

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

#spliting the data into trian and test splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=2)

X.shape

X_train.shape

X_test.shape

"""##Model Selcetion And Trianing

XGBOOST
"""

model = XGBRegressor()
model.fit(X_train, y_train)

"""Evalution"""

training_data_pred = model.predict(X_train)

#R Squared metric
train_R2_score = metrics.r2_score(training_data_pred, y_train)
#Mean absolute Error
MAE_train = metrics.mean_absolute_error(training_data_pred, y_train)

print(f"R2 score on trianing data is {train_R2_score}")
print(f"Mean Absolute Error score on trianing data is {MAE_train}")

#R Squared metric
test_R2_score = metrics.r2_score(model.predict(X_test), y_test)
#Mean absolute Error
MAE_test = metrics.mean_absolute_error(model.predict(X_test), y_test)

print(f"R2 score on test data is {test_R2_score}")
print(f"Mean Absolute Error score on test data is {MAE_test}")

!pip install catboost

from catboost import CatBoostRegressor
regressor = CatBoostRegressor()
regressor.fit(X_train, y_train)

#R Squared metric
test_R2_score = metrics.r2_score(regressor.predict(X_test), y_test)
#Mean absolute Error
MAE_test = metrics.mean_absolute_error(regressor.predict(X_test), y_test)

print(f"R2 score on test data is {test_R2_score}")
print(f"Mean Absolute Error score on test data is {MAE_test}")