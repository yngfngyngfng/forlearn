import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def asamble_df():
    dirname = 'esaccounts'
    dfsum = pd.DataFrame()
    for filename in os.listdir(dirname):
        if '.json' in filename:
            filename = os.path.join(dirname, filename)
            print('process: ', filename)
            df = pd.read_json(filename)
            print(df.shape, df.columns)
            dfsum = dfsum.append(df)
            print(dfsum.shape)
    dfsum.to_excel('dfsum.xls')

if __name__ == '__main__':
    asamble_df()