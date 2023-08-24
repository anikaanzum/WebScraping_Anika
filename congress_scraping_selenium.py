import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
output_file='congressbill.csv'
# this parameter tells Chrome that
# it should be run without UI (Headless)
# options.add_argument("-headless") 
url = 'https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22search%22%3A%22congressId%3A118%20AND%20billStatus%3A%5C%22Introduced%5C%22%20environment%22%7D'

# using Firefox headless webdriver to secure connection to Firefox 
with webdriver.Firefox() as driver: 
    # opening the target website in the browser 
    driver.get(url) 
 
    #printing the target website url and title 
    print(driver.current_url) # https://scrapeme.live/shop/ 
    print(driver.title) # Products - ScrapeMe
    # print(driver.page_source)
    # a = driver.find_elements_by_class_name()
    list_webdriver=driver.find_elements(By.CLASS_NAME, "expanded")
    # a=a.find_elements(By.CLASS_NAME, "expanded")
    # print(a)
    rows=[]
    for i in list_webdriver:
        row=i.text.split("\n")
        rows.append(row)


with open(output_file, 'w') as f:
    write = csv.writer(f)
    # write.writerow(fields)
    write.writerows(rows)
