import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22search%22%3A%22congressId%3A118%20AND%20billStatus%3A%5C%22Introduced%5C%22%20environment%22%7D').read()
soup = bs.BeautifulSoup(source,'lxml')
# title of the page
print(soup.title)

# # get attributes:
# print(soup.title.name)

# # get values:
# print(soup.title.string)

# # beginning navigation:
# print(soup.title.parent.name)

# # getting specific values:
# print(soup.p)
# print(soup.find_all('p'))
# for paragraph in soup.find_all('p'):
#     print(paragraph.string)
#     print(str(paragraph.text))

# for url in soup.find_all('a'):
#     print(url.get('href'))

# print(soup.get_text())
