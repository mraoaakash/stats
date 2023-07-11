import pandas as pd
import numpy as np
import os 
import re


df = pd.read_csv('tnbc.csv')
# arrange all the data in ascending order
# df = df.sort_values(by=['image'])
# df.reset_index(drop=True, inplace=True)
print(len(df))
# filtering the data
tnbc_lst = df['image'].tolist()
tnbc_lst = [x.lower() for x in tnbc_lst]
tnbc_lst = [i.replace(".tif","").replace("-","_") for i in tnbc_lst]
split_list = np.array([])
for i in tnbc_lst:
    i = np.array(i.split("_"))
    split_list = np.concatenate((split_list, i), axis=0)

split_list = [x for x in split_list if not x.isdigit() and len(x) >1]
split_list = np.unique(split_list)

# split_list = np.array(split_list)

print(split_list)
