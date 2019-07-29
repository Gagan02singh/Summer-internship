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
import requests
from urllib3.exceptions import ProtocolError

path_to_screenshot = 'D:\\Summer_RA\\Screenshots'
path_to_csv = 'D:\\Summer_RA\\Code\\Data\\Batch\\Batch1\\batch1_new_2.csv'
path_to_driver = 'D:\\Summer_RA\\Code\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
path_to_log = 'D:\\Summer_RA\\Code\\Data\\Batch\\Batch1\\batch1_log.txt'

bp_links_df  = pd.read_csv(path_to_csv)
driver = webdriver.PhantomJS(path_to_driver)
no_of_timeouts = 0
timeout=30
driver.set_page_load_timeout(timeout)
others = 0


def green_color_optimized(screenpath):
    img = image.load_img(screenpath,target_size=(300,300,3))
    x = image.img_to_array(img)
    count_green = 0
    count_white =0
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
          elif (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255):
            count_white+=1
    denominator = (x.shape[0]*x.shape[1]) - count_white
    return round(100*(count_green/denominator),2)


def driver_initialize(width,height):
    
  print(timeout)
  #driver.set_page_load_timeout(timeout)
  #driver.implicitly_wait(timeout)
 # driver.set_script_timeout(30)
  
  driver.set_window_size(width, height)
   
     
def driver_screenshot(row):
    try:
        print(row['Company'], row['Id'],row['Date'])
        global no_of_timeouts
        global others
        global driver
        
        path = path_to_screenshot + "/" + row['Company'][0][0].lower() + "/" + row['Company']+ "/"
        if not os.path.exists(path):
            os.makedirs(path)
        filename = row['Company'] + row["Date"]+ ".png"
        screen_path =  os.path.join(path, filename)
        
        driver.get(row["new_url"])
        driver.execute_script("window.scrollTo(0, 1024)") 
        print("execute")
        #time.sleep(30)
        driver.save_screenshot(screen_path)
        print("successful {}".format(row["Id"]))
        return green_color_optimized(screen_path)
    
    except(ProtocolError, AttributeError):
        print("protocol error")
        driver.quit()
        driver = webdriver.PhantomJS(path_to_driver)
    except:
        message = "{} occured.".format(sys.exc_info()[0])
        if ("Timeout" in message):
            no_of_timeouts+=1
        else:
            others+=1
        if ("MaxRetryError" in message):
            driver.quit()
            driver = webdriver.PhantomJS(path_to_driver)
        print(message)
        print(row['Company'], row['Id'],row['Date']+ "failed")
        
  
def driver_quit():
  driver.quit()
  




driver_initialize(1366,1024)
bp_links_df['green'] = bp_links_df.query("Id >= 462").apply(driver_screenshot,axis=1)

driver_quit()

#bp_links_df.to_csv("D:\\Summer_RA\\Code\\" + path_to_csv.split(".")[0]+"_output"+".csv", index= False)
print("no. of timeouts", no_of_timeouts)
print("--- {} seconds ---".format(round(time.time() - start_time,2)))