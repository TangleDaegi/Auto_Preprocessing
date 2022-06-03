
import pandas as pd


def def_data_divide(df_input, column, num_divide, bins, labels):
    #print(column)
    #print(num_divide)
    #print(bins)
    #print(labels)
    result = pd.cut(df_input['{}'.format(column)], bins, right=True, labels=labels)
    return result
