
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

def SendRequest(url):
	
	try:
	    page = requests.get(url,timeout=10)
	except requests.exceptions.Timeout:
	    print("Timeout occured")

	return page


arg=sys.argv[1]

main_url='https://www.youtube.com'
sub_url='/results?search_query='
query= arg

url = main_url+sub_url+query


page=SendRequest(url)
soup = BeautifulSoup(page.content, 'html.parser')


titleList = soup.find_all('div', attrs={'id': 'title-wrapper'})

postTitles=[]
postLinks=[]
upvotes=[]
comments=[]


for i in titleList:
	
	# postTitles.append(i.find('h3').text)
	# postLinks.append(main_url+i.find('a', href=True)['href'])
	print(i)

# reactionList = soup.find_all('span', attrs={'class': '_vaFo96phV6L5Hltvwcox'})



# for i in reactionList:

# 	if "upvotes" in i.text or "upvote" in i.text:
# 		a=i.text
# 		upvotes.append(a.split(' ')[0])
# 	if "comments" in i.text or "comment" in i.text:
# 		s=i.text
# 		comments.append(s.split(' ')[0])


# dict = {'title': postTitles, 'link': postLinks, 'like': upvotes, 'comment': comments}

# # print(len(postTitles),len(postLinks),len(upvotes),len(comments))

# df = pd.DataFrame(dict)
# print(df)

# df.to_csv(query+'.csv')

	
