class Listing:
    def __init__(self, title, location, size, price, link):
        self.title = title
        self.location = location
        #self.size = size
        self.price = price
        self.link = link
    
    def __str__(self):
        return f"{self.title} {self.location} {self.price} {self.link}"

import requests
import csv
from bs4 import BeautifulSoup

url = 'https://washingtondc.craigslist.org/search/silver-spring-md/apa?lat=39.0553&laundry=1&lon=-77.0201&max_bedrooms=1&max_price=1550&search_distance=8.9#search=1~gallery~0~0'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

listings = soup.find_all('li', class_='cl-static-search-result')

listing_objects = []

for listing in listings:
    title = listing.find('div', class_='title').text.strip()
    price = listing.find('div', class_='price').text.strip()
    location_tag = listing.find('div', class_='location')
    location = location_tag.text.strip() if location_tag else "Location not specified"
    link = listing.find('a')['href']
    listing_objects.append(Listing(title, location, price, location, link))

for listing in listing_objects:
    print("Title:", listing.title)
    print("Price:", listing.price)
    print("Link:", listing.link)
    print()

with open('listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price", "Location", "Link"])
    for listing in listing_objects:
        writer.writerow([listing.title, listing.price, listing.location, listing.link])
