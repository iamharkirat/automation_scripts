import pandas as pd
import os

path = os.path.dirname(__file__)
dirs = os.listdir(path)

dataframes=[]
merge=pd.DataFrame()

for _file in dirs:
    if _file[-4:] == '.csv':
        dataframes.append(path.replace("\\", '/') + "/" +_file)

for file in dataframes:
    df=pd.read_csv(file)
    merge=merge.append(df, ignore_index=True)

merge.to_csv('Merged_File.csv')

