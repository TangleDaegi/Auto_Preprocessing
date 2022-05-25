from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

def def_StandardScaler(df_input, column):
    scaler = StandardScaler()
    result = scaler.fit_transform(df_input[['{}'.format(column)]])
    return result

def def_MinMaxScaler(df_input, column):
    scaler = MinMaxScaler()
    result = scaler.fit_transform(df_input[['{}'.format(column)]])
    return result
