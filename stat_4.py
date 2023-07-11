import pandas as pd
import numpy as np
import os 
import re
import cv2
import warnings
warnings.filterwarnings("ignore")


df_master = pd.read_csv('tnbc.csv')
# print(df_master)

tnbc_lst = df_master['image'].tolist()
tnbc_lst = [x.upper() for x in tnbc_lst]
tnbc_lst = [i.replace(".","_").replace("-","_") for i in tnbc_lst]
split_list = []
for i in tnbc_lst:
    i = i.split("_")
    split_list.append(i)
# print(split_list)

# finding the longest subarray
max_len = 0
for i in split_list:
    if len(i) > max_len:
        max_len = len(i)
# print(max_len)

# padding the subarrays with max_len 0s at the beginning
for i in split_list:
    while len(i) < max_len:
        i.insert(0,"NaN")
    for j in range(len(i)):
        if i[j] == 'SU' or i[j] == 'SURGE'or i[j] == 'SURGERY' or i[j] == 'SX':
            i[j] = 'SURGERY'
        if i[j] =='BIOPSY' or i[j] =='BIOSPY' or i[j] == 'BIPSY'or i[j] == 'BX':
            i[j] = 'BIOPSY'
        if i[j] == 'HER2' or i[j] == 'HER':
            i[j] = 'HER2'
        if i[j] == 'ER' or i[j] == 'E':
            i[j] = 'ER'
        if i[j] == 'TNBC' or i[j] == 'YNBC':
            i[j] = 'TNBC'
        if i[j] == 'HNE' or i[j] == 'H&E' or i[j] == 'HNE':
            i[j] = 'H&E'
        if i[j] == 'KI67' or i[j] == 'KI':
            i[j] = 'KI67'
        if "CD" in i[j]:
            i[j] = "CD31"
        if "VI" in i[j]:
            i[j] = "VIMENTIN"



# for i in split_list:
#     print(i)


# saving the split_list as a csv file
df = pd.DataFrame(split_list)
df.to_csv('tnbc_split.csv', index=False, header=False)

frame = pd.DataFrame(columns=['image','path', 'date','subtype','stain','SX/BX', 'magnification', 'dimension','size', 'rem_info'])


for row, i in enumerate(split_list):
    data = np.array(split_list[row])
    data_org = np.array(df_master.iloc[row])
    # print(data)
    # print(data_org)
    dic = {}
    dic['image'] = data_org[0]
    dic['path'] = data_org[1]
    dic['date'] = [x for x in data if re.search(r'\d{6}', x)][0] if len([x for x in data if re.search(r'\d{6}', x)])>0  else 'NaN'
    try:
        data = data.tolist()
        data.remove(dic['date'])
        data = np.array(data)
    except:
        pass
    dic['subtype'] = [x for x in data if x == 'TNBC' or x == 'HER2' or x == 'ER'][0] if len([x for x in data if x == 'TNBC' or x == 'HER2' or x == 'ER'])>0 else 'NaN'
    try:
        data = data.tolist()
        data.remove(dic['subtype'])
        data = np.array(data)
    except:
        pass
    staining =  ['yap', 'vimentin', 'vim', 'h&e', 'hne','cd31', 'ck5', 'ck516', 'ck56','ki', 'ki67','egfr','HER3']
    staining = [x.upper() for x in staining]
    stain = [x for x in data if x in staining]
    dic['stain'] = stain[0] if len(stain)>0 else 'NaN'
    try:
        data = data.tolist()
        data.remove(dic['stain'])
        data = np.array(data)
    except:
        pass
    dic['SX/BX'] = [x for x in data if x == 'SURGERY' or x == 'BIOPSY'][0] if len([x for x in data if x == 'SURGERY' or x == 'BIOPSY'])>0 else 'NaN'
    try:
        data = data.tolist()
        data.remove(dic['SX/BX'])
        data = np.array(data)
    except:
        pass
    dic['magnification'] = [x for x in data if x == '20X' or x == '40X' or x == '60X' or x == '100X'][0] if len([x for x in data if x == '20X' or x == '40X' or x == '60X' or x == '100X'])>0 else '40X'
    try:
        data = data.tolist()
        data.remove(dic['magnification'])
        data = np.array(data)
    except:
        pass
    try:
        data = data.tolist()
        data.remove('NaN')
        data.remove('TIF')
        dic['rem_info'] = '_'.join(data)
    except:
        pass

    try:
        image = dic['path'] 
        image = cv2.imread(image)
        dic['dimension'] = image.shape
        dic['size'] = image.size
    except:
        pass
    # print(data)
    print(dic)
    frame = frame.append(dic, ignore_index=True)
print(frame)
frame.to_csv('tnbc_new_split.csv', index=False, header=True)


