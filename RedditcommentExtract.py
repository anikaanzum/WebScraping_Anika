# This code tries to scrap comments from reddit posts and analyze public sentiment 
# but this is not a successful code as we need Reddit python API to do comment extract and analysis
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import io
import codecs 
import os
import sys
import re
import xmltojson

import urllib.request as urllib2
from bs4 import *
from urllib.parse  import urljoin

from nrclex import NRCLex


def SendRequest(url):
	
	try:
	    page = requests.get(url,timeout=10)
	except requests.exceptions.Timeout:
	    print("Timeout occured")

	return page

#function to read from csv file and do sentimental analysis using TextBlob library


def Comment_Extract(url):
    page=SendRequest(url)
    with open('file.html', 'w') as file:
        file.write(page.text)
    soup = BeautifulSoup(page.content, 'html.parser')

    # titleList = soup.findAll('shreddit-comment',class_"")
    # print()
    commentList = soup.find_all(attrs={"class" : "sidebar-grid pdp grid justify-items-center mx-auto \
        grid-cols-1 gap-x-md \
        xs:grid-cols-8 xs:gap-x-lg xs:mx-md \
        s:grid-cols-12 \
        m:grid-cols-14 m:mx-lg \
        l:grid-cols-16 l:max-w-container-l l:mx-auto \
        xl:grid-cols-18 xl:max-w-container-xl \
      "})
    print(commentList)
    comment=[]
    for i in commentList:
        comment.append(i.string)
        # print(sentiment_analysis(i.string))
    print(comment)
    # return comment



def crawl(pages, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = urllib2.urlopen(page)
                except:
                    print( "Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read())
                links = soup('a') #finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.append(url)
        pages = indexed_url
    return indexed_url




pagelist=["https://www.reddit.com/r/technology/comments/12ewvo1/the_newest_version_of_chatgpt_passed_the_us/"]
urls = crawl(pagelist, depth=1)
print( urls )
# print(Comment_Extract('https://www.reddit.com/r/technology/comments/12ewvo1/the_newest_version_of_chatgpt_passed_the_us/'))