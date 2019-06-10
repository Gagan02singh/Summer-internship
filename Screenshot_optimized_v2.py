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



path_to_screenshot = 'D:\Summer_RA\Screenshots'
path_to_csv = 'D:/Summer_RA/Code/waybackLinkV1.csv'
path_to_driver = 'C:/Users/singh/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe'

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
    filename = row['Company'] + row['URL'].split("/")[4] + ".png"
    screen_path =  os.path.join(path_to_screenshot, filename)
    driver.get(row['URL'])
    driver.save_screenshot(screen_path)
    return green_color_optimized(screen_path)
    
  
def driver_quit():
  driver.quit()
  


start_time = time.time()

driver_initialize(1024,768)
bp_links_df['green'] = bp_links_df.head(10).apply(driver_screenshot,axis=1)

driver_quit()

print("--- {} seconds for image capturing ---".format(round(time.time() - start_time),2))