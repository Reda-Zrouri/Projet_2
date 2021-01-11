#import module

import requests 
from requests import get
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

results = requests.get(url)
soup = BeautifulSoup(results.text, "html.parser")

product_page_url = []
universal_product_code = []
title = []
price_including_tax = []
price_excluding_tax = []
number_available = []
product_description = []
category = []
review_rating = []
image_url = []

if results.ok:
	
	name = soup.find('title')
	title.append(name)

	upc = soup.findAll('td')
	universal_product_code.append(upc)

	excl = soup.findAll('td')
	price_excluding_tax.append(excl)

	inclu = soup.findAll('td')
	price_including_tax.append(inclu)

	nbr = soup.findAll('td')
	number_available.append(nbr)

	dsp = soup.findAll('p')
	product_description.append(dsp)

	ctg = soup.findAll('a')
	category.append(ctg)


print(url)
print(name.text)
print(upc[0].text)
print(excl[2].text)
print(inclu[3].text)
print(nbr[5].text)
print(dsp[3].text)
print(ctg[3].text)
