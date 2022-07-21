# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 23:42:18 2022

@author: Adithya Raj Mishra
"""

from webscrapping_yt import scrapComments,scrapLinkAddresses,initDriver
import time
import pandas as pd
import json
driver = initDriver(True)
webLinks = scrapLinkAddresses('https://www.youtube.com/c/TaylorSwift/videos',100,driver)
time.sleep(4)

with open('taylor_meta.txt','w') as metaFile:
    metaFile.write('')
with open('taylor_comments.txt','w') as commentFile:
    commentFile.write('')

counter = 0
for i in webLinks:
    comments,meta = scrapComments(i,True,driver)
    tableI = pd.DataFrame(comments,columns=['Comments','Likes'])
    with open('taylor_meta.txt','a') as metaFile:
        metaFile.write('\n'+json.dumps(meta))
    with open('taylor_comments.txt','a') as commentFile:
        commentFile.write('\n'+tableI.to_json())
    time.sleep(1)
    counter+=1
    print(counter,'/',100)
    

