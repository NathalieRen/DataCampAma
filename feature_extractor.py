# -*- coding: utf-8 -*-
"""
Created on Sat Jul 04 11:44:12 2015

@author: NR705624
"""
import numpy as np
import pandas as pd
import os

class FeatureExtractor(object):
    def __init__(self):
        pass

    def fit(self, X_df, y_array):
        pass

    def transform(self, X_df):
        X_encoded = X_df
        
        #data_oil = pd.read_csv("./DataLake/data_oil.csv")
        path = os.path.dirname(__file__)
        data_oil = pd.read_csv(os.path.join(path, "data_oil.csv"))
        #data_oil = data_oil.rename(columns={'Date': 'DateOfDeparture'})
        
        #data = pd.merge(X_df, data_oil, on='DateOfDeparture')     
        data = X_encoded.merge(data_oil, how='left', left_on=['DateOfDeparture'], right_on=['Date'], sort=False)       
        data = data.drop('Date', axis=1)
        
        data_encoded = data

        data_encoded = data_encoded.join(pd.get_dummies(data_encoded['Departure'], prefix='d'))
        data_encoded = data_encoded.join(pd.get_dummies(data_encoded['Arrival'], prefix='a'))
        data_encoded = data_encoded.drop('Departure', axis=1)
        data_encoded = data_encoded.drop('Arrival', axis=1)

        data_encoded['DateOfDeparture'] = pd.to_datetime(data_encoded['DateOfDeparture'])
        data_encoded['year'] = data_encoded['DateOfDeparture'].dt.year
        data_encoded['month'] = data_encoded['DateOfDeparture'].dt.month
        data_encoded['day'] = data_encoded['DateOfDeparture'].dt.day
        data_encoded['weekday'] = data_encoded['DateOfDeparture'].dt.weekday
        data_encoded['week'] = data_encoded['DateOfDeparture'].dt.week
        data_encoded['n_days'] = data_encoded['DateOfDeparture'].apply(lambda date: (date - pd.to_datetime("1970-01-01")).days)

        data_encoded = data_encoded.join(pd.get_dummies(data_encoded['year'], prefix='y'))
        data_encoded = data_encoded.join(pd.get_dummies(data_encoded['month'], prefix='m'))
        data_encoded = data_encoded.join(pd.get_dummies(data_encoded['day'], prefix='d'))
        data_encoded = data_encoded.join(pd.get_dummies(data_encoded['weekday'], prefix='wd'))
        data_encoded = data_encoded.join(pd.get_dummies(data_encoded['week'], prefix='w'))

        features = data_encoded.drop(['DateOfDeparture'], axis=1)
        X_array = features.values
        
        return X_array