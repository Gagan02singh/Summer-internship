# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:14:15 2019

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
from time import sleep

import asyncio

path_to_screenshot = 'D:\Summer_RA\Screenshots'
path_to_csv = 'D:/Summer_RA/Code/waybackLinkV1.csv'
path_to_driver = 'C:/Users/singh/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe'

bp_links_df  = pd.read_csv(path_to_csv)
driver = webdriver.PhantomJS(path_to_driver)

def driver_initialize(width,height):
  driver.set_script_timeout(30)
  if width and height:
        driver.set_window_size(width, height)
   
     
async def driver_screenshot(row):
    print("Thread started")
    filename = row.split("/")[4] + ".png"
    screen_path =  os.path.join(path_to_screenshot, filename)
    driver.get(row)
    driver.save_screenshot(screen_path)
    #return green_color_optimized(screen_path)
    
  
def driver_quit():
  driver.quit()
  
async def start_parallel():
    tasks = [driver_screenshot(i) for i in bp_links_df['URL'].head(5).tolist()]
    await asyncio.gather(*tasks)

  
driver_initialize(1024,768)

start_time = time.time()
asyncio.run(start_parallel())
print("--- {} seconds for image capturing ---".format(round(time.time() - start_time),2))

driver_quit()