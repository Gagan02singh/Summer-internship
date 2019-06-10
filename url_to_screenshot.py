# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:44:59 2019

@author: singh
"""

"""from selenium import webdriver

DRIVER = 'C:/Users/singh/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(DRIVER)
driver.get('https://www.spotify.com')
screenshot = driver.save_screenshot('C:/Users/singh/Desktop/my_screenshot.png')
driver.quit()

"""

import os
from subprocess import Popen, PIPE
from selenium import webdriver

"""abspath = lambda *p: os.path.abspath(os.path.join(*p))
ROOT = abspath(os.path.dirname(__file__))
"""
"""
def execute_command(command):
    result = Popen(command, shell=True, stdout=PIPE).stdout.read()
    if len(result) > 0 and not result.isspace():
        raise Exception(result)
"""

def do_screen_capturing(url, screen_path, width, height):
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

"""
def do_crop(params):
    print "Croping captured image.."
    command = [
        'convert',
        params['screen_path'],
        '-crop', '%sx%s+0+0' % (params['width'], params['height']),
        params['crop_path']
    ]
    execute_command(' '.join(command))
"""
"""
def do_thumbnail(params):
    print "Generating thumbnail from croped captured image.."
    command = [
        'convert',
        params['crop_path'],
        '-filter', 'Lanczos',
        '-thumbnail', '%sx%s' % (params['width'], params['height']),
        params['thumbnail_path']
    ]
    execute_command(' '.join(command))
"""

def get_screen_shot(**kwargs):
    url = kwargs['url']
    width = int(kwargs.get('width', 1024)) # screen width to capture
    height = int(kwargs.get('height', 768)) # screen height to capture
    #filename = kwargs.get('filename', 'screen.png') # file name e.g. screen.png
   # path = kwargs.get('path', ROOT) # directory path to store screen
    screen_path = 'C:/Users/singh/Desktop/my_screenshot.png'
    do_screen_capturing(url, screen_path, width, height)
    return screen_path
    """
    crop = kwargs.get('crop', False) # crop the captured screen
    crop_width = int(kwargs.get('crop_width', width)) # the width of crop screen
    crop_height = int(kwargs.get('crop_height', height)) # the height of crop screen
    crop_replace = kwargs.get('crop_replace', False) # does crop image replace original screen capture?

    thumbnail = kwargs.get('thumbnail', False) # generate thumbnail from screen, requires crop=True
    thumbnail_width = int(kwargs.get('thumbnail_width', width)) # the width of thumbnail
    thumbnail_height = int(kwargs.get('thumbnail_height', height)) # the height of thumbnail
    thumbnail_replace = kwargs.get('thumbnail_replace', False) # does thumbnail image replace crop image?
"""
    #screen_path = abspath(path, filename)
    #screen_path = 'C:/Users/singh/Desktop/my_screenshot.png'
    
"""
   crop_path = thumbnail_path = screen_path

    if thumbnail and not crop:
        raise Exception, 'Thumnail generation requires crop image, set crop=True'
"""
    
"""
    if crop:
        if not crop_replace:
            crop_path = abspath(path, 'crop_'+filename)
        params = {
            'width': crop_width, 'height': crop_height,
            'crop_path': crop_path, 'screen_path': screen_path}
        do_crop(params)

        if thumbnail:
            if not thumbnail_replace:
                thumbnail_path = abspath(path, 'thumbnail_'+filename)
            params = {
                'width': thumbnail_width, 'height': thumbnail_height,
                'thumbnail_path': thumbnail_path, 'crop_path': crop_path}
            do_thumbnail(params)
            """
    #return screen_path, crop_path, thumbnail_path
    

if __name__ == '__main__':
    '''
        Requirements:
        Install NodeJS
        Using Node's package manager install phantomjs: npm -g install phantomjs
        install selenium (in your virtualenv, if you are using that)
        install imageMagick
        add phantomjs to system path (on windows)
    '''

    url = 'https://web.archive.org/web/20190201133720/https://www.bp.com/'
    
    """screen_path, crop_path, thumbnail_path = get_screen_shot(
        url=url, filename='sof.png',
        crop=True, crop_replace=False,
        thumbnail=True, thumbnail_replace=False,
        thumbnail_width=200, thumbnail_height=150,
    )"""
    screen_path = get_screen_shot(url=url, filename='sof.png')