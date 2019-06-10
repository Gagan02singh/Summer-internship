# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:10:53 2019

@author: singh
"""

import os
from subprocess import Popen, PIPE
from selenium import webdriver
import time
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
from keras.preprocessing import image
import os
import zipfile
import matplotlib.pyplot as plt
import pandas as pd


os.chdir('D:\Summer_RA\Screenshots')
path = os.getcwd()

bp_links_df  = pd.read_csv('D:/Summer_RA/Code/waybackLinkV1.csv')
driver = webdriver.PhantomJS('C:/Users/singh/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')


def green_vectorized(screenpath):
  img = image.load_img(screenpath,target_size=(300,300,3))
  x = image.img_to_array(img)
  mask = (x[:,:,1] > x[:,:,0]) & (x[:,:,1] > x[:,:,2]) & ((x[:,:,1]/np.sum(x, axis=2)) > .35)
  #print(mask)
  return round(100 * np.sum(mask)/(x.shape[0]*x.shape[1]), 2)


def driver_initialize(width,height):
  driver.set_script_timeout(30)
  if width and height:
        driver.set_window_size(width, height)
   
     
def driver_screenshot(df):
    green =[]
    for index, row in df.iterrows():
        filename = row['Company'] + row['URL'].split("/")[4] + ".png"
        screen_path =  os.path.join(path, filename)
        driver.get(row['URL'])
        driver.save_screenshot(screen_path)
        green.append(green_vectorized(screen_path))
    return green
    
  
def driver_quit():
  driver.quit()
  


start_time = time.time()

driver_initialize(1024,768)
green = driver_screenshot(bp_links_df.head(10))
driver_quit()

print("--- {} seconds for image capturing ---".format(round(time.time() - start_time),2))