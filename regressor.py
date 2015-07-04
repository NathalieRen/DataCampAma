# -*- coding: utf-8 -*-
"""
Created on Sat Jul 04 11:47:54 2015

@author: NR705624
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.base import BaseEstimator

class Regressor(BaseEstimator):
    def __init__(self):
        self.clf = RandomForestRegressor(n_estimators=316, max_depth=50, max_features=10)

    def fit(self, X, y):
        self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict(X)