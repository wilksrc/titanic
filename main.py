# is this how you installed lightgbm?
# https://www.geeksforgeeks.org/how-to-install-xgboost-and-lightgbm-on-macos/


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import lightgbm as lgbm
import mytools

# import data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
train.rename(columns=str.lower, inplace=True)
test.rename(columns=str.lower, inplace=True)

# metadata
print('train dim: ' + str(train.shape))
print('test dim: ' + str(test.shape))
train.info()

train['rec'] = 1

# create categories for numerics with too many levels
train['age_g1'] = pd.qcut(x=train['age'], q=7).astype(str)
train['fare_g1'] = pd.qcut(x=train['fare'], q=7).astype(str)

# predictor list
ls_predictors = ['pclass', 'sex', 'age_g1', 'sibsp', 'parch', 'fare_g1', 'embarked']

################ univariate ################
train_stack_summary = mytools.onewaysummary(df_input=train, xvars=ls_predictors, target='survived', exposure='rec', boo_stack=True)
mytools.onewayplot(df_input=train_stack_summary, barvar='rec', linevar='freq')

