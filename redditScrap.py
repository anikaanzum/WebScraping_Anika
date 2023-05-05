
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

# python argument pass
arg=sys.argv[1]

main_url='https://www.reddit.com'
sub_url='/search/?q='
query= arg

url = main_url+sub_url+query


page=SendRequest(url)
soup = BeautifulSoup(page.content, 'html.parser')

# fetch titles and links of the posts
titleList = soup.find_all('div', attrs={'class': '_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen'})

postTitles=[]
postLinks=[]
upvotes=[]
comments=[]


for i in titleList:
	
	postTitles.append(i.find('h3').text)
	postLinks.append(main_url+i.find('a', href=True)['href'])

# fetch like comment count from each post
reactionList = soup.find_all('span', attrs={'class': '_vaFo96phV6L5Hltvwcox'})



for i in reactionList:

	if "upvotes" in i.text or "upvote" in i.text:
		a=i.text
		upvotes.append(a.split(' ')[0])
	if "comments" in i.text or "comment" in i.text:
		s=i.text
		comments.append(s.split(' ')[0])


dict = {'title': postTitles, 'link': postLinks, 'like': upvotes, 'comment': comments}

# print(len(postTitles),len(postLinks),len(upvotes),len(comments))

df = pd.DataFrame(dict)
print(df)

# save data to csv file
df.to_csv(query+'.csv')

	
