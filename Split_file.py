# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

path_to_csv = 'D:\\Summer_RA\\Code\\Data\\Batch\\Batch1\\batch1_new_0.csv'
#path_to_csv = 'D:\\Summer_RA\\Code\\Data\\1-4000_cleaned.csv'

bp_links_df  = pd.read_csv(path_to_csv)

""" Subsetting the file"""
"""
bp_links_df_subset = bp_links_df.query("Id > 500 and Id <= 1500")
bp_links_df_subset.to_csv("D:\\Summer_RA\\Code\\Data\\Batch\\Batch2\\batch2_501_1500.csv",index = False)
"""                           

"""splittin files into multiple files"""
"""
df_split = np.array_split(bp_links_df,6)

for i in range(len(df_split)):
    df_split[i].to_csv("D:\\Summer_RA\\Code\\Data\\Batch\\Batch2\\batch2_new_{}.csv".format(i),index = False)

"""
"""
#picking random samples
for i in range(15):
    random_sample = bp_links_df.sample(n=1000)
    random_sample.to_csv("D:\\Summer_RA\\Code\\Data\\sample{}.csv".format(i),index = False)
#sample_1.columns = ['URL' 'Date' 'Company' 'Id']
#data_excluding_sample_5_30= pd.concat([bp_links_df, sample_5_30, sample_5_30]).drop_duplicates(keep=False)

"""


#checking for %OA records

bp_links_df  = pd.read_csv(path_to_csv)
bp_links_df_subset = bp_links_df[bp_links_df['new_url'].str.contains("%")==True]