import pandas as pd
import numpy as np

from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from typing import Tuple, Union, List

class DelayModel:

    def __init__(self):
        self._model = LogisticRegression()  # Model should be saved in this attribute.

    def preprocess(self, data: pd.DataFrame, target_column: str = None) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:

        # Use apply along with a lambda function to convert each date string to a datetime object
        data['Fecha-O'] = data['Fecha-O'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        data['Fecha-I'] = data['Fecha-I'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        
        # Now calculate the minute difference directly within the DataFrame
        data['min_diff'] = (data['Fecha-O'] - data['Fecha-I']).dt.total_seconds() / 60
        
        threshold_in_minutes = 15
        data['delay'] = np.where(data['min_diff'] > threshold_in_minutes, 1, 0)
        
        features_base = pd.concat([
            pd.get_dummies(data['OPERA'], prefix = 'OPERA'),
            pd.get_dummies(data['TIPOVUELO'], prefix = 'TIPOVUELO'), 
            pd.get_dummies(data['MES'], prefix = 'MES')], 
            axis = 1
        )
        
        top_10_features = [
            "OPERA_Latin American Wings", 
            "MES_7",
            "MES_10",
            "OPERA_Grupo LATAM",
            "MES_12",
            "TIPOVUELO_I",
            "MES_4",
            "MES_11",
            "OPERA_Sky Airline",
            "OPERA_Copa Air"
        ]

        features = features_base[top_10_features]

        if target_column:
            target = data[[target_column]]
            return features, target
        return features

    def fit(self, features: pd.DataFrame, target: pd.DataFrame) -> None:
        self._model.fit(features, target.values.ravel())

    def predict(self, features: pd.DataFrame) -> List[int]:
        # Convert the predicted values to Python int type
        return [int(value) for value in self._model.predict(features)]
