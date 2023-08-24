import requests

url = 'https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22search%22%3A%22congressId%3A118%20AND%20billStatus%3A%5C%22Introduced%5C%22%20environment%22%7D'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers, timeout=10)
print(response.content)
with open('file.html', 'w') as file:
    file.write(response.text)


# challenges:
#1. got 403 Forbidden error because the site doesn't allow scripting requests/sending requests via code.
#2.  I used header to make the requests like a browser to avoid 403 forbidden error. They designed the web architecture such a way to 
# avoid the fake browser requests. 
#The server sends a response to my request with a lot of subdomains for next level requests. 


