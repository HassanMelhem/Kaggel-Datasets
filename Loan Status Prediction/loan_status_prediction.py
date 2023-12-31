# -*- coding: utf-8 -*-
"""Loan_Status_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fcdrrXtILve_fsrEJ9ODHdNt9lC7aCx6

Importing The Dependencies
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# %matplotlib inline

"""Data Collection and Preprocessing"""

# loading the dataset to dataframe
# download the dataset from https://www.kaggle.com/datasets/ninzaami/loan-predication
df = pd.read_csv('train_dataset.csv')
df.head()

df.shape

df.describe()

# number of missing values in dataframe
df.isnull().sum()

df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
df['Married'].fillna(df['Married'].mode()[0],inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0],inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0],inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)
df = df.drop(['Loan_ID'], axis = 1)

df.shape

# label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])
df.head()

df['Dependents'] .value_counts()

# replace 3+ to 4
df['Dependents'].replace(to_replace='3+', value=4, inplace=True)
df.Dependents.value_counts()

df.info()

df['Dependents'] = df['Dependents'].astype(int)

df.info()

sns.countplot(x="Credit_History",hue='Gender', data=df, palette="viridis")

sns.countplot(x="Property_Area", data=df, palette="cubehelix")

df = pd.get_dummies(df)
df.head()

df.drop(['Gender_Female', 'Married_No', 'Education_Not Graduate', 'Self_Employed_No', 'Property_Area_Rural' ], axis=1, inplace=True)

X = df.drop(["Loan_Status"], axis=1)
y = df["Loan_Status"]

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=2)

## Trianing the model SVM
classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_train)
accuracy_score(y_pred, y_train)

y_pred = classifier.predict(X_test)
accuracy_score(y_pred, y_test)

