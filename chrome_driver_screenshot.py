# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:13:57 2019

@author: singh
"""
"""
from selenium import webdriver

url = 'http://wayback.archive.org/web/20131018144323/http://www.infosonics.com:80/'
path = 'D:\\Summer_RA\\Code\\scrape.png'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600') 

driver = webdriver.Chrome(executable_path = 'D:\\Summer_RA\\Code\\chromedriver.exe', chrome_options = options)
driver.get(url)
el = driver.find_element_by_tag_name('body')
el.screenshot(path)
driver.quit()
"""

from internetarchive import download
download('gatewaycasinosincomefund.com', verbose=True)