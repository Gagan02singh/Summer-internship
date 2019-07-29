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




def get_redirect_url(row):
   try:    
       r = requests.get(row["URL"])
       return r.url
   except:
       print("{} occured at {} {}".format(sys.exc_info()[0],row["Date"],row["Id"]))
       
start_time = time.time()
for i in range(6,14):
    path_to_csv = '/home/g_singh/test/sample{}.csv'.format(i)
    bp_links_df  = pd.read_csv(path_to_csv)
        
    bp_links_df['new_url'] = bp_links_df.apply(get_redirect_url,axis=1)
    bp_links_df.to_csv("/home/g_singh/test/sample{}_new.csv".format(i),index = False)

print("--- {} seconds ---".format(round(time.time() - start_time,2)))


"""
r = requests.get("http://wayback.archive.org/web/20050701074015/http://www.honeywell.com:80/")
print(r.url)
"""