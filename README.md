# WebScraping

## Congress.gov Webscraping

We started webscraping using `requests` python library. However, Congress.gov site blocks the python web requests by sending `HTTP:403 Forbidden`. We even tried to send the requests by adding headers. We found two options to get `congress.gov` data.


### api.congress.gov

 Congress.gov Application Programming Interface (API) provides a method for Congress and the public to view, retrieve, and re-use machine-readable data from collections available on Congress.gov. [The repository](https://github.com/LibraryOfCongress/api.congress.gov/) contains information on accessing and using the beta Congress.gov API, as well as documentation on available endpoints.

Here is the [Python example](https://github.com/LibraryOfCongress/api.congress.gov/tree/main/api_client/python). 


### [Selenium](https://pythonbasics.org/selenium-firefox/)

We also used `selenium` to scrap data from congress.gov. 

#### Prerequisite

```
python3 -m pip install -r requirements.txt
```

#### Scraping

- Open `congress_scraping_selenium.py` and edit `url` variable with the desired URL
- change `output_file` variable with desired CSV file name
- run `python3 congress_scraping_selenium.py`

