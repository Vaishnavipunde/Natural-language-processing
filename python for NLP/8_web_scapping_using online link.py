# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:20:49 2023

@author: rajendra
"""

from bs4 import BeautifulSoup as bs
# Importing the BeautifulSoup module for HTML parsing.

import requests
# Importing the requests module to send HTTP requests.

link = "https://www.flipkart.com/canon-eos-m50-mark-ii-mirrorless-camera-ef-m15-45mm-stm-lens/p/itm7a4f536cb1255?pid=DLLGFY7XYG8YFMQT&lid=LSTDLLGFY7XYG8YFMQTSG43XC&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&fm=organic&iid=731ce7d3-d04e-4794-89f1-44e2a8290b8b.DLLGFY7XYG8YFMQT.SEARCH&ppt=hp&ppn=homepage&ssid=zqzv2ykomo0000001701746565787"
# The URL of the Flipkart page from which data is to be scraped.

page = requests.get(link)
# Using requests.get() to fetch the HTML content of the provided URL.

page 
page.content
# These lines appear to fetch the page content but don't store or use the retrieved content.

soup = bs(page.content, 'html.parser')
# Creating a BeautifulSoup object for parsing the HTML content of the page.

print(soup.prettify())
# Printing the prettified HTML content of the page.

#get title of rating
title=soup.find_all('p',class_='_2-N8zT')
title
reviewd_title=[]
for i in range (0,len(title)):
    reviewd_title.append(title[i].get_text())
reviewd_title

len(reviewd_title)


#get star of rating
rating=soup.find_all("div",class_="_3LWZlK _1BLPMq")
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)

rate.append('')
rate.append('')
rate.append('')
len(rate)



body=soup.find_all('div',class_='t-ZTKy')
body
reviewd_body=[]
for i in range (0,len(body)):
    reviewd_body.append(body[i].get_text())
reviewd_body

len(reviewd_body)




import pandas as pd
df=pd.DataFrame()
df['review_title']=reviewd_title
df['rate']=rate
df['review_body']=reviewd_body
df


df.to_csv("C:\1-python\python for NLP/webscapping.csv",index=True)
from textblob import TextBlob
sent="This is very excellent garden"
plo=TextBlob(sent).sentiment.polarity
poldf=pd.read_csv("C:\1-python\python for NLP/webscapping.csv")
df.head()
df["polarity"]=df["review"]
apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']






















