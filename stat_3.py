import pandas as pd
import numpy as np
import random as rand
import os 
import re


df = pd.read_csv('tnbc.csv')
# filter for name containing -er- or _er_ or -er_ or _er-
df_ER = df[df['image'].str.contains('-ER-|_ER_|-ER_|_ER-')]
df_ER = df_ER[df_ER['image'].str.contains('hne|HnE|HNE')]
df_ER = df_ER.sort_values(by=['image'])
df_ER = df_ER.reset_index(drop=True)
df_HER2 = df[df['image'].str.contains('-HER2-|_HER2_|-HER2_|_HER2-')]
df_HER2 = df_HER2[df_HER2['image'].str.contains('hne|HnE|HNE')]
df_HER2 = df_HER2.sort_values(by=['image'])
df_HER2 = df_HER2.reset_index(drop=True)
df_TNBC = df[df['image'].str.contains('-TNBC-|_TNBC_|-TNBC_|_TNBC-')]
df_TNBC = df_TNBC[df_TNBC['image'].str.contains('hne|HnE|HNE')]
df_TNBC = df_TNBC.sort_values(by=['image'])
df_TNBC = df_TNBC.reset_index(drop=True)

# print(len(df_ER))
# print(df_ER.head())
# print(len(df_HER2))
# print(df_HER2.head())  
# print(len(df_TNBC))
# print(df_TNBC.head())
# setting seed and producing random number
rand.seed(99)
integer_rand = rand.randint(0, len(df_ER)-1)
print(integer_rand)

images = [df_ER.iloc[integer_rand]["path"],df_HER2.iloc[integer_rand]["path"],df_TNBC.iloc[integer_rand]["path"]]
print(images)