import requests
from bs4 import BeautifulSoup

url = 'https://washingtondc.craigslist.org/search/silver-spring-md/apa?lat=39.0553&laundry=1&lon=-77.0201&max_bedrooms=1&max_price=1550&search_distance=8.9#search=1~gallery~0~0'

html = requests.get(url)

print(html.text)