# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:10:53 2019

@author: singh
"""
import sys
import os
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
from keras.preprocessing import image
import os
import pandas as pd

path_to_screenshot = '/mnt/data/test/screenshots'
path_to_csv = sys.argv[1]

bp_links_df  = pd.read_csv(path_to_csv)

def green_color_optimized(row):
    filename = row['Company'] + row["Date"]+ ".png"
    path = os.path.join(path_to_screenshot,row['Company'][0][0].lower() , row['Company'],filename)
    img = image.load_img(path,target_size=(300,300,3))
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
    if denominator != 0:
      return round(100*(count_green/denominator),2)


bp_links_df['green'] = bp_links_df.iloc[:8000,].apply(green_color_optimized,axis=1)


bp_links_df.to_csv('/mnt/data/test/output/batch1/' + path_to_csv.split("/")[-1].split(".")[0] + "_output" + ".csv", index= False)
