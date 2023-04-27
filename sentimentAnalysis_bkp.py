
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
from nrclex import NRCLex


def SendRequest(url):
	
	try:
	    page = requests.get(url,timeout=10)
	except requests.exceptions.Timeout:
	    print("Timeout occured")

	return page

#function to read from csv file and do sentimental analysis using TextBlob library
def analyse():
    df=pd.read_csv('amazon_review.csv')
    df.dropna(inplace=True)

    sentiment=[]
    rating=[]
    for index, sum in (df.iterrows()):
        blob=tb(sum['Summary'])
        sentiment.append(blob.sentiment.polarity)
        rating.append(int(sum['Rating']))

    #using normal distribution to get probability of positive response for a product
    x=np.array(sentiment)
    mean=np.mean(x)
    sd=np.std(x)
    cdf_upper_limit=norm(mean,sd).cdf(1)
    cdf_lower_limit=norm(mean,sd).cdf(0)
    prob=(cdf_upper_limit-cdf_lower_limit)*100
    print("The mean is: ",round((mean)*100,2))
    print(f'The probablity that the person has a sentiment polarity between 0 to 1 is : {round(prob,2)}%')

    y=np.array(rating)
    mean2=np.mean(y)
    prob2=(mean2/5)*100
    print(f'The average rating is : {round(mean2,2)} ie {round(prob2,2)}%')
    mat.scatter(x,norm.pdf(x,mean,sd))
    mat.show()

url = 'https://www.reddit.com/r/technology/comments/12ewvo1/the_newest_version_of_chatgpt_passed_the_us/'
page=SendRequest(url)
soup = BeautifulSoup(page.content, 'html.parser')

# titleList = soup.findAll('shreddit-comment',class_"pt-md px-md xs:px-0")

commentList = soup.body.findAll(['p'])

comment=[]
for i in commentList:
    comment.append(i.string)
    # print(sentiment_analysis(i.string))
print(comment)
