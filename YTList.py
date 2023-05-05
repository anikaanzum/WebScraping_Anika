# from requests_html import HTMLSession 
# from bs4 import BeautifulSoup as bs # importing BeautifulSoup
# import xmltojson

# #fetching titles and thumbnail img data using BeautifulSoup but YT doesn't allow to scrap all the title and img
# # sample youtube video url
# video_url = "https://www.youtube.com/results?search_query=chatgpt"
# # init an HTML Session
# session = HTMLSession()
# # get the html content
# response = session.get(video_url)
# # execute Java-script
# response.html.render(sleep=1)
# # create bs object to parse HTML
# soup = bs(response.html.html, "html.parser")

# # meta=soup.find_all("div",attrs={'id':'contents','class': 'style-scope ytd-section-list-renderer'})
# titleList=soup.find_all("h3")

# imgList = soup.find_all('img')

# for i in titleList:
# 	print(i.text)
# 	print("************")
	
# for i in imgList:
# 	print(i.get('src'))
# 	print("************")

# for i in meta:
# 	print(i)


# fetch metadata for YT search results
# resource link : https://github.com/alexmercerind/youtube-search-python
from youtubesearchpython import VideosSearch, ResultMode

videosSearch = VideosSearch('algebra', limit = 2)

print(videosSearch.result())

print('**************')
# get YT video suggestions
from youtubesearchpython import Suggestions

suggestions = Suggestions(language = 'en', region = 'US')

print(suggestions.get('algebra', mode = ResultMode.json))