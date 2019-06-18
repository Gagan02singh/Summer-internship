# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:10:53 2019

@author: singh
"""
import sys
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



path_to_screenshot = '/home/g_singh/test/screenshots'
path_to_csv = 
path_to_driver = '/home/g_singh/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'

bp_links_df  = pd.read_csv(path_to_csv)
driver = webdriver.PhantomJS(path_to_driver)


def green_color_optimized(screenpath):
    img = image.load_img(screenpath,target_size=(300,300,3))
    x = image.img_to_array(img)
    count_green = 0
    for i in range(0,x.shape[0]):
      for j in range(0,x.shape[1]):
        pixel = list(map(int, x[i,j].tolist()))
        if sum(pixel) != 0:
          green_pixel = 100*(pixel[1]/sum(pixel))
          blue_pixel = 100*(pixel[2]/sum(pixel))
          red_pixel = 100*(pixel[0]/sum(pixel))
          if green_pixel > red_pixel and green_pixel > blue_pixel:
            if green_pixel > 35:
              count_green += 1
    return round(100*(count_green/(x.shape[0]*x.shape[1])),2)


def driver_initialize(width,height):
  driver.set_script_timeout(30)
  if width and height:
        driver.set_window_size(width, height)
   
     
def driver_screenshot(row):
    path = path_to_screenshot + "/" + row['Company'][0][0].lower() + "/" + row['Company']+ "/"
    if not os.path.exists(path):
        os.makedirs(path)
    filename = row['Company'] + row["Date"]+ ".png"
    screen_path =  os.path.join(path, filename)
    driver.get(row['URL'])
    driver.save_screenshot(screen_path)
    return green_color_optimized(screen_path)
    
  
def driver_quit():
  driver.quit()
  


start_time = time.time()

driver_initialize(1024,768)
bp_links_df['green'] = bp_links_df.apply(driver_screenshot,axis=1)

driver_quit()

bp_links_df.to_csv(path_to_csv.split(".")[0]+".csv", index= False)

print("--- {} seconds for {} ---".format(round(time.time() - start_time,2),sys.argv[1]))