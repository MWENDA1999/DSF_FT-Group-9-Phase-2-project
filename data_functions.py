# data_functions.py

import pandas as pd
import numpy as np

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def explore_data(data):
    data_info = data.info()
    data_desc = data.describe()
    return data_info, data_desc

def clean_data(data):
    # Drop unnecessary columns
    dCol = ['id', 'date', 'zipcode']
    data.drop(dCol, axis=1, inplace=True)
    
    # Feature Engineering
    waterfront_mapping = {'NO': 0, 'YES': 1}
    view_mapping = {
        'NONE': 0,
        'FAIR': 1,
        'AVERAGE': 2,
        'GOOD': 3,
        'EXCELLENT': 4
    }
    condition_mapping = {
        'Poor': 1,
        'Fair': 2,
        'Good': 3,
        'Average': 4,
        'Very Good': 5
    }
    
    data['view'] = data['view'].map(view_mapping)
    data['waterfront'] = data['waterfront'].map(waterfront_mapping)
    data['condition'] = data['condition'].map(condition_mapping)
    
    data['grade'] = data['grade'].str.extract('(\d+)').astype(int)
    
    # Convert 'sqft_basement' to numerical and replace missing values
    data['sqft_basement'] = pd.to_numeric(data['sqft_basement'], errors='coerce')
    mean = data['sqft_basement'].mean()
    data['sqft_basement'].fillna(mean, inplace=True)
    
    return clean_data

def remove_missing_values(data):
    data = data.dropna()
    return data


def sort_data_by_price(data):
    data_sorted = data.sort_values("price", ascending=False).head(10)
    return data_sorted
