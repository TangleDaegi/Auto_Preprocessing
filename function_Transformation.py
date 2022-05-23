import pandas as pd
import numpy as np

def StandardScaler(df, column):
    return df[column].apply(lambda x: (x-x.mean())/ x.std(), axis=0)




def modType(column, option):
    if option == "Default":
        return column

    elif option == "Numeric":
        return pd.to_numeric(column)

    elif option == "Categorical":
        return column.astype('category')

    elif option  == "Datetime":
        return pd.to_datetime(column)


def handleMissingVal(column, option):
    if option == "Do Notiong":
        return column
    elif option == "Replacing With Mean":
        column.fillna(int(column.mean()), inplace=True)
        return column
    elif option == "Replacing With Median":
        column.fillna(int(column.median()), inplace =True)
        return column