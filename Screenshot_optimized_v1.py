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


os.chdir('D:\Summer RA\Screenshots')
path = os.getcwd()

bp_links_df  = pd.read_csv('D:/Smu/SMUWorks/bp.com.csv',header= None)
bp_links_df.columns = ['links']
links = bp_links_df.links.tolist()


images =[]
driver = webdriver.PhantomJS('C:/Users/singh/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')


def green_color_optimized(screenpath):
    start_time = time.time()
    img = image.load_img(screenpath,target_size=(300,300,3))
    x = image.img_to_array(img)
    print("Image size: ", x.shape)
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
    green_percent = round(100*(count_green/(x.shape[0]*x.shape[1])),2)
    print(green_percent)
    print("--- {} seconds for image processing ---".format(round(time.time() - start_time),2))
    return green_percent
#    print("No. of green pixels: ",count_green)


def driver_initialize(width,height):
  driver.set_script_timeout(30)
  if width and height:
        driver.set_window_size(width, height)
   
     
def driver_screenshot(urls):
  green_color=[]
  for i in urls:
    print(i)
    filename = i.split("/")[4] + ".png"
    screen_path =  os.path.join(path, filename)
    images.append(screen_path)
    driver.get(i)
    driver.save_screenshot(screen_path)
    
    green_color.append(green_color_optimized(screen_path))
  return green_color
    
  
def driver_quit():
  driver.quit()
  




start_time = time.time()
driver_initialize(1024,768)

green_color = driver_screenshot(links)
driver_quit()
print("--- {} seconds for image capturing ---".format(round(time.time() - start_time),2))
print(len(green_color))