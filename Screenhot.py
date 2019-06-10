# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:47:33 2019

@author: singh
"""

import os
from subprocess import Popen, PIPE
from selenium import webdriver
import time
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
from keras.preprocessing import image

os.chdir('D:\Summer RA\Screenshots')
path = os.getcwd()

def do_screen_capturing(url, screen_path, width, height):
    start_time = time.time()
   # print "Capturing screen.."
    driver = webdriver.PhantomJS('C:/Users/singh/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    # it save service log file in same directory
    # if you want to have log file stored else where
    # initialize the webdriver.PhantomJS() as
    # driver = webdriver.PhantomJS(service_log_path='/var/log/phantomjs/ghostdriver.log')
    driver.set_script_timeout(30)
    if width and height:
        driver.set_window_size(width, height)
    driver.get(url)
    driver.save_screenshot(screen_path)
    driver.quit()
    print("--- {} seconds for capturing ---".format(round(time.time() - start_time),2))
    
def get_screen_shot(**kwargs):
    url = kwargs['url']
    width = int(kwargs.get('width', 1024)) # screen width to capture
    height = int(kwargs.get('height', 768)) # screen height to capture
    filename = kwargs.get('filename', 'screen.png') # file name e.g. screen.png
   # path = kwargs.get('path', ROOT) # directory path to store screen
    screen_path =  os.path.join(path, filename)
    do_screen_capturing(url, screen_path, width, height)
    return screen_path

def green_color(screenpath):
    start_time = time.time()
    img = image.load_img(screenpath)
    x = image.img_to_array(img)
    print("Image size: ", x.shape)
    count_green = 0
    for i in range(0,x.shape[0]):
      for j in range(0,x.shape[1]):
        pixel = list(map(int, x[i,j].tolist()))
        if sum(pixel) != 0:
          if 100*(pixel[1]/sum(pixel)) > 35:
            count_green += 1
    print(round(100*(count_green/(x.shape[0]*x.shape[1])),2))
    print("No. of green pixels: ",count_green)
    print("--- {} seconds for processing image---".format(round(time.time() - start_time),2))

if __name__ == '__main__':
    
     url = 'http://wayback.archive.org/web/20141202013935/http://www.bp.com/'
     screen_path = get_screen_shot(url=url, filename='test.png')
     green_color(screen_path)