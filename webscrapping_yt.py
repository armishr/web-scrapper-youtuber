# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 23:28:40 2022

@author: Adithya Raj Mishra
"""
#webscrapper successful :) 
#gets details of yt video  given the link
#just need to add getting the likes for each comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time

path = r"C:\Users\Adithya Raj Mishra\Documents\Misc_2\chromedriver_win32\chromedriver.exe"
def initDriver(headLess):
    '''initialise driver'''
    options = Options()
    options.headless = headLess
    #chrome_options = Options()
    options.add_argument("window-size=1920,1080")
    
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service = service,options = options)
    return driver
    
def scrapComments(pgAddr,getMeta,driver):
    '''Gets the comment list for a particular webpage'''
    
   #options = Options()
   #options.headless = True
   #chrome_options = Options()
   #options.add_argument("window-size=1920,1080")
    
   #service = Service(executable_path=path)
   #driver = webdriver.Chrome(service = service,options = options)
    website = pgAddr
    driver.get(website)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(1)
    creator = driver.find_element(by = 'xpath',value = '//ytd-channel-name[@class = "style-scope ytd-video-owner-renderer"]/div/div/yt-formatted-string/a').text
    
    subscribers = driver.find_element(by = 'xpath',value = '//yt-formatted-string[@id="owner-sub-count"]').text
    
    noOfComments = driver.find_element(by = 'xpath',value = '//ytd-comments-header-renderer/div/h2/yt-formatted-string/span').text
    views = driver.find_element(by ='xpath',value ='//span[@class = "view-count style-scope ytd-video-view-count-renderer"]').text
    likes = driver.find_element(by = 'xpath',value = '//div[(@class = "style-scope ytd-video-primary-info-renderer") and (@id = "menu")]/ytd-menu-renderer/div/ytd-toggle-button-renderer/a/yt-formatted-string').get_attribute('aria-label')
    
    time.sleep(2)
    title = driver.find_element(by = 'xpath',value = '//yt-formatted-string[@class = "style-scope ytd-video-primary-info-renderer"]').text
    
    print("Downloading comments of video: "+title+" by "+creator)
    #now will try to scrap all the comments
    noOfComments = noOfComments.replace(',', '')
    noOfComments = (int)(noOfComments)
    
    commentElements = []
    likeElements = []
    minT =min(100,int(noOfComments)/5)
    minT = int(minT)
    for i in range(0,minT):
        driver.execute_script("window.scrollTo(0, 1600+1600*{times});".format(times = i))
        time.sleep(0.1)
        
       
    commentElements = driver.find_elements(by = 'xpath',value = "//div[@class='style-scope ytd-expander']/yt-formatted-string")
    likeElements = driver.find_elements(by='xpath',value = "//span[@id = 'vote-count-middle']")    
    print(len(commentElements))
    commentList = [(commentElements[i].text,likeElements[i].get_attribute('aria-label')) for i in range(len(commentElements))]
    #driver.close()
    if(getMeta == False):
        return commentList
    else:
        return (commentList,[title,creator,subscribers,views,likes,str(noOfComments)+' comments'])

def scrapLinkAddresses(pgAddr,target,driver):
    '''To get list of video links'''
    website = pgAddr
    #options = Options()
    #options.headless = True
    #chrome_options = Options()
    #options.add_argument("window-size=1920,1080")
    
    #service = Service(executable_path=path)
    #driver = webdriver.Chrome(service = service,options = options)
    
    driver.get(website)
    time.sleep(1)
    elementList = []
    i = 0
    while(len(elementList)<target):
        driver.execute_script("window.scrollTo(0, 1600+800*{times});".format(times = i))
        time.sleep(1)
        elementList = driver.find_elements(by = 'xpath',value='//div[@class = "style-scope ytd-grid-video-renderer"][@id = "dismissible"]/ytd-thumbnail/a')
        i+=1
        print(len(elementList),'/',target)
    print('WebLinks extracted!!')
    linkList = [(j.get_attribute("href")) for j in elementList]
   
    #driver.close()
    
    
    return linkList

