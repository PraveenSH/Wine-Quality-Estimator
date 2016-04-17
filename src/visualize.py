import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as pp

train_df = pd.read_csv('../input/train-red.csv', header=0)
test_df = pd.read_csv('../input/test-red.csv', header=0)

train_y = train_df['quality']
test_y = test_df['quality']

feat = train_df['residual sugar']
pp.plot(feat, len(feat)*[1], "x")
pp.show()
