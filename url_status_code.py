# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:44:59 2019

@author: singh
"""

import sys
import urllib.request as urllib2
import requests
import pandas as pd
import time


"""

def get_redirect_url(row):
   try:    
       r = requests.get(row["URL"].strip())
       print(row["URL"])
       print(row["Company"],row["Date"])
       print("{} successful".format(r.url))
       return r.url
   except:
       print("{} occured at {} {}".format(sys.exc_info()[0],row["Date"],row["Id"]))
       
start_time = time.time()
path_to_csv = 'D:\\Summer_RA\\url_status_test.csv'
bp_links_df  = pd.read_csv(path_to_csv)
bp_links_df['new_url'] = bp_links_df.apply(get_redirect_url,axis=1)
bp_links_df.to_csv("D:\\Summer_RA\\url_status_test_new.csv",index = False)

print("--- {} seconds ---".format(round(time.time() - start_time,2)))

"""


r = requests.get("http://wayback.archive.org/web/20050203120348/http://www.adpselect.com:80/")
print(r.url)

"""
path_to_csv = 'D:\\Summer_RA\\Code\\Data\\Batch\\Batch2\\batch2_501_1500.csv'
bp_links_df  = pd.read_csv(path_to_csv)
bp_links_df['Company'] = bp_links_df['Company'].apply(lambda x : x.replace("/","_"))
bp_links_df.to_csv("D:\\Summer_RA\\Code\\Data\\Batch\\Batch2\\batch2_501_1500_new.csv",index = False)
"""