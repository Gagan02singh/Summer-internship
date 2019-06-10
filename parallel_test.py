# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:59:37 2019

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
from multiprocessing import Process
from threading import Thread
from time import sleep

threads = []



path_to_screenshot = 'D:\Summer_RA\Screenshots'
path_to_csv = 'D:/Summer_RA/Code/waybackLinkV1.csv'
path_to_driver = 'C:/Users/singh/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe'

bp_links_df  = pd.read_csv(path_to_csv)
driver = webdriver.PhantomJS(path_to_driver)


def driver_initialize(width,height):
  driver.set_script_timeout(30)
  if width and height:
        driver.set_window_size(width, height)
   
     
def driver_screenshot(row):
    filename = row.split("/")[4] + ".png"
    screen_path =  os.path.join(path_to_screenshot, filename)
    driver.get(row)
    driver.save_screenshot(screen_path)
    #return green_color_optimized(screen_path)
    
  
def driver_quit():
  driver.quit()
  
 
start_time = time.time()
driver_initialize(1024,768)

for i in bp_links_df['URL'].head(5).tolist():
     print("Thread Started")
     p = Thread(target=driver_screenshot, args=[i.strip()])
     p.start()
     threads.append(p)



  # block until all the threads finish (i.e. block until all function_x calls finish)    
for t in threads:
    t.join()

"""for i in bp_links_df['URL'].head(10).tolist():
    driver_screenshot(i)
 """    
driver_quit()
print("--- {} seconds for image capturing ---".format(round(time.time() - start_time),2))