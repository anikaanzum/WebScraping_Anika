
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
import sys
from RedditcommentExtract import *
arg=sys.argv[1]

main_url = 'https://www.reddit.com'
sub_url="/search/?q="
url=main_url+sub_url+arg

page=SendRequest(url)
soup = BeautifulSoup(page.content, 'html.parser')

videoList = soup.find_all('div', class_= '_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen')

data=[]
for i in videoList:
	print("*******************")
	title=i.find('h3').text
	link=main_url+i.find('a', href=True)['href']
	print(title)
	print(link)
	print(Comment_Extract(link))
	data.append([title,link])

# print(data)