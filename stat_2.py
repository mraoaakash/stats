import pandas as pd
import numpy as np
import os 
import re


df = pd.read_csv('tnbc.csv')
biopsy = ['biopsy', 'biospy', 'bipsy', 'bx']
print(biopsy[i].upper for i in range(len(biopsy)))
surgery = ['su', 'surge', 'surgery', 'sx']
subtypes = ['er','her', 'her2', 'her3', 'tnbc', 'ynbc']
staining =  ['yap', 'vimentin', 'vim', 'h&e', 'hne', 'ihc','cd31', 'ck5', 'ck516', 'ck56','ki', 'ki67','egfr' ]
magnification = ['10x', '20x', '40x', '60x', '100x']

er_num = 0
er_yap_num = 0
er_vim_num = 0
er_hne_num = 0
er_cd31_num = 0
er_ck5_num = 0
er_ck516_num = 0
er_ck56_num = 0
er_ki_num = 0
er_ki67_num = 0
er_egfr_num = 0
er_10x_num = 0
er_20x_num = 0
er_40x_num = 0
er_60x_num = 0
er_100x_num = 0
er_surgery_num = 0
er_biopsy_num = 0
er_ihc_num = 0

her2_num = 0
her2_yap_num = 0
her2_vim_num = 0
her2_hne_num = 0
her2_cd31_num = 0
her2_ck5_num = 0
her2_ck516_num = 0
her2_ck56_num = 0
her2_ki_num = 0
her2_ki67_num = 0
her2_egfr_num = 0
her2_10x_num = 0
her2_20x_num = 0
her2_40x_num = 0
her2_60x_num = 0
her2_100x_num = 0
her2_surgery_num = 0
her2_biopsy_num = 0
her2_ihc_num = 0

her3_num = 0
her3_yap_num = 0
her3_vim_num = 0
her3_hne_num = 0
her3_cd31_num = 0
her3_ck5_num = 0
her3_ck516_num = 0
her3_ck56_num = 0
her3_ki_num = 0
her3_ki67_num = 0
her3_egfr_num = 0
her3_10x_num = 0
her3_20x_num = 0
her3_40x_num = 0
her3_60x_num = 0
her3_100x_num = 0
her3_surgery_num = 0
her3_biopsy_num = 0
her3_ihc_num = 0

tnbc_num = 0
tnbc_yap_num = 0
tnbc_vim_num = 0
tnbc_hne_num = 0
tnbc_cd31_num = 0
tnbc_ck5_num = 0
tnbc_ck516_num = 0
tnbc_ck56_num = 0
tnbc_ki_num = 0
tnbc_ki67_num = 0
tnbc_egfr_num = 0
tnbc_10x_num = 0
tnbc_20x_num = 0
tnbc_40x_num = 0
tnbc_60x_num = 0
tnbc_100x_num = 0
tnbc_surgery_num = 0
tnbc_biopsy_num = 0
tnbc_ihc_num = 0



# arrange all the data in ascending order
df = df.sort_values(by=['image'])
df.reset_index(drop=True, inplace=True)
print(len(df))
# filtering the data to subtype
tnbc_lst = df['image'].tolist()
tnbc_lst = [x.lower() for x in tnbc_lst]
tnbc_lst = [i.replace(".tif","").replace("-","_") for i in tnbc_lst]
split_list = np.array([])
for i in tnbc_lst:
    split_list = i.split("_")
    if "tnbc" in split_list:
        tnbc_num += 1
        if "yap" in split_list:
            tnbc_yap_num += 1
        if "vimentin" in split_list or "vim" in split_list:
            tnbc_vim_num += 1
        if "hne" in split_list or "h&e" in split_list:
            tnbc_hne_num += 1
        if "cd31" in split_list:
            tnbc_cd31_num += 1
        if "ck5" in split_list:
            tnbc_ck5_num += 1
        if "ck516" in split_list:
            tnbc_ck516_num += 1
        if "ck56" in split_list:
            tnbc_ck56_num += 1
        if "ki" in split_list:
            tnbc_ki_num += 1
        if "ki67" in split_list:
            tnbc_ki67_num += 1
        if "egfr" in split_list:
            tnbc_egfr_num += 1
        if "10x" in split_list:
            tnbc_10x_num += 1
        if "20x" in split_list:
            tnbc_20x_num += 1
        if "40x" in split_list:
            tnbc_40x_num += 1
        if "60x" in split_list:
            tnbc_60x_num += 1
        if "100x" in split_list:
            tnbc_100x_num += 1
        if 'su' in split_list or 'surge' in split_list or 'surgery' in split_list or 'sx' in split_list:
            tnbc_surgery_num += 1
        if 'biopsy'in split_list or 'biospy'in split_list or 'bipsy'in split_list or 'bx' in split_list:
            tnbc_biopsy_num += 1
        if 'ihc' in split_list:
            tnbc_ihc_num += 1
        # print(i)
    if "er" in split_list:
        er_num += 1

        if "yap" in split_list:
            er_yap_num += 1
        if "vimentin" in split_list or "vim" in split_list:
            er_vim_num += 1
        if "hne" in split_list or "h&e" in split_list:
            er_hne_num += 1
        if "cd31" in split_list:
            er_cd31_num += 1
        if "ck5" in split_list:
            er_ck5_num += 1
        if "ck516" in split_list:
            er_ck516_num += 1
        if "ck56" in split_list:
            er_ck56_num += 1
        if "ki" in split_list:
            er_ki_num += 1
        if "ki67" in split_list:
            er_ki67_num += 1
        if "egfr" in split_list:
            er_egfr_num += 1
        if "10x" in split_list:
            er_10x_num += 1
        if "20x" in split_list:
            er_20x_num += 1
        if "40x" in split_list:
            er_40x_num += 1
        if "60x" in split_list:
            er_60x_num += 1
        if "100x" in split_list:
            er_100x_num += 1
        if 'su' in split_list or 'surge' in split_list or 'surgery' in split_list or 'sx' in split_list:
            er_surgery_num += 1
        if 'biopsy'in split_list or 'biospy'in split_list or 'bipsy'in split_list or 'bx' in split_list:
            er_biopsy_num += 1
        if 'ihc' in split_list:
            er_ihc_num += 1
        # print(i)

    if "her" in split_list:
        her2_num += 1
        if "yap" in split_list:
            her2_yap_num += 1
        if "vimentin" in split_list or "vim" in split_list:
            her2_vim_num += 1
        if "hne" in split_list or "h&e" in split_list:
            her2_hne_num += 1
        if "cd31" in split_list:
            her2_cd31_num += 1
        if "ck5" in split_list:
            her2_ck5_num += 1
        if "ck516" in split_list:
            her2_ck516_num += 1
        if "ck56" in split_list:
            her2_ck56_num += 1
        if "ki" in split_list:
            her2_ki_num += 1
        if "ki67" in split_list:
            her2_ki67_num += 1
        if "egfr" in split_list:
            her2_egfr_num += 1
        if "10x" in split_list:
            her2_10x_num += 1
        if "20x" in split_list:
            her2_20x_num += 1
        if "40x" in split_list:
            her2_40x_num += 1
        if "60x" in split_list:
            her2_60x_num += 1
        if "100x" in split_list:
            her2_100x_num += 1
        if 'su' in split_list or 'surge' in split_list or 'surgery' in split_list or 'sx' in split_list:
            her2_surgery_num += 1
        if 'biopsy'in split_list or 'biospy'in split_list or 'bipsy'in split_list or 'bx' in split_list:
            her2_biopsy_num += 1
        if 'ihc' in split_list:
            her2_ihc_num += 1
        # print(i)
    if "her2" in split_list:
        her2_num += 1
        if "yap" in split_list:
            her2_yap_num += 1
        if "vimentin" in split_list or "vim" in split_list:
            her2_vim_num += 1
        if "hne" in split_list or "h&e" in split_list:
            her2_hne_num += 1
        if "cd31" in split_list:
            her2_cd31_num += 1
        if "ck5" in split_list:
            her2_ck5_num += 1
        if "ck516" in split_list:
            her2_ck516_num += 1
        if "ck56" in split_list:
            her2_ck56_num += 1
        if "ki" in split_list:
            her2_ki_num += 1
        if "ki67" in split_list:
            her2_ki67_num += 1
        if "egfr" in split_list:
            her2_egfr_num += 1
        if "10x" in split_list:
            her2_10x_num += 1
        if "20x" in split_list:
            her2_20x_num += 1
        if "40x" in split_list:
            her2_40x_num += 1
        if "60x" in split_list:
            her2_60x_num += 1
        if "100x" in split_list:
            her2_100x_num += 1
        if 'su' in split_list or 'surge' in split_list or 'surgery' in split_list or 'sx' in split_list:
            her2_surgery_num += 1
        if 'biopsy'in split_list or 'biospy'in split_list or 'bipsy'in split_list or 'bx' in split_list:
            her2_biopsy_num += 1
        if 'ihc' in split_list:
            her2_ihc_num += 1
        # print(i)
    if "her3" in split_list:
        her3_num += 1
        if "yap" in split_list:
            her3_yap_num += 1
        if "vimentin" in split_list or "vim" in split_list:
            her3_vim_num += 1
        if "hne" in split_list or "h&e" in split_list:
            her3_hne_num += 1
        if "cd31" in split_list:
            her3_cd31_num += 1
        if "ck5" in split_list:
            her3_ck5_num += 1
        if "ck516" in split_list:
            her3_ck516_num += 1
        if "ck56" in split_list:
            her3_ck56_num += 1
        if "ki" in split_list:
            her3_ki_num += 1
        if "ki67" in split_list:
            her3_ki67_num += 1
        if "egfr" in split_list:
            her3_egfr_num += 1
        if "10x" in split_list:
            her3_10x_num += 1
        if "20x" in split_list:
            her3_20x_num += 1
        if "40x" in split_list:
            her3_40x_num += 1
        if "60x" in split_list:
            her3_60x_num += 1
        if "100x" in split_list:
            her3_100x_num += 1
        if 'su' in split_list or 'surge' in split_list or 'surgery' in split_list or 'sx' in split_list:
            her3_surgery_num += 1
        if 'biopsy'in split_list or 'biospy'in split_list or 'bipsy'in split_list or 'bx' in split_list:
            her3_biopsy_num += 1
        if 'ihc' in split_list:
            her3_ihc_num += 1
        # print(i)
    if "ynbc" in split_list:
        tnbc_num += 1
        if "yap" in split_list:
            tnbc_yap_num += 1
        if "vimentin" in split_list or "vim" in split_list:
            tnbc_vim_num += 1
        if "hne" in split_list or "h&e" in split_list:
            tnbc_hne_num += 1
        if "cd31" in split_list:
            tnbc_cd31_num += 1
        if "ck5" in split_list:
            tnbc_ck5_num += 1
        if "ck516" in split_list:
            tnbc_ck516_num += 1
        if "ck56" in split_list:
            tnbc_ck56_num += 1
        if "ki" in split_list:
            tnbc_ki_num += 1
        if "ki67" in split_list:
            tnbc_ki67_num += 1
        if "egfr" in split_list:
            tnbc_egfr_num += 1
        if "10x" in split_list:
            tnbc_10x_num += 1
        if "20x" in split_list:
            tnbc_20x_num += 1
        if "40x" in split_list:
            tnbc_40x_num += 1
        if "60x" in split_list:
            tnbc_60x_num += 1
        if "100x" in split_list:
            tnbc_100x_num += 1
        if 'su' in split_list or 'surge' in split_list or 'surgery' in split_list or 'sx' in split_list:
            tnbc_surgery_num += 1
        if 'biopsy'in split_list or 'biospy'in split_list or 'bipsy'in split_list or 'bx' in split_list:
            tnbc_biopsy_num += 1
        if 'ihc' in split_list:
            tnbc_ihc_num += 1
        # print(i)



tnbc_stats = [tnbc_num, tnbc_yap_num, tnbc_vim_num, tnbc_hne_num, tnbc_cd31_num, tnbc_ck5_num, tnbc_ck516_num, tnbc_ck56_num, tnbc_ki_num, tnbc_ki67_num, tnbc_egfr_num, tnbc_10x_num, tnbc_20x_num, tnbc_40x_num, tnbc_60x_num, tnbc_100x_num, tnbc_surgery_num, tnbc_biopsy_num, tnbc_ihc_num]
er_stats = [er_num, er_yap_num, er_vim_num, er_hne_num, er_cd31_num, er_ck5_num, er_ck516_num, er_ck56_num, er_ki_num, er_ki67_num, er_egfr_num, er_10x_num, er_20x_num, er_40x_num, er_60x_num, er_100x_num, er_surgery_num, er_biopsy_num, er_ihc_num]
her2_stats = [her2_num, her2_yap_num, her2_vim_num, her2_hne_num, her2_cd31_num, her2_ck5_num, her2_ck516_num, her2_ck56_num, her2_ki_num, her2_ki67_num, her2_egfr_num, her2_10x_num, her2_20x_num, her2_40x_num, her2_60x_num, her2_100x_num, her2_surgery_num, her2_biopsy_num, her2_ihc_num]
her3_stats = [her3_num, her3_yap_num, her3_vim_num, her3_hne_num, her3_cd31_num, her3_ck5_num, her3_ck516_num, her3_ck56_num, her3_ki_num, her3_ki67_num, her3_egfr_num, her3_10x_num, her3_20x_num, her3_40x_num, her3_60x_num, her3_100x_num, her3_surgery_num, her3_biopsy_num, her3_ihc_num]

stats_df = pd.DataFrame([tnbc_stats, er_stats, her2_stats, her3_stats], columns = ["total", "yap", "vimentin", "hne", "cd31", "ck5", "ck516", "ck56", "ki", "ki67", "egfr", "10x", "20x", "40x", "60x", "100x", "surgery", "biopsy", "IHC"], index = ["tnbc", "er", "her2", "her3"])
stats_df = stats_df.transpose()
stats_df.to_csv("stats.csv")
print(stats_df)