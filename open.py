#import module

import requests 
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
reponse = requests.get(url)
if reponse.ok: 
	soup = BeautifulSoup(reponse.text, 'lxml')
	tds = soup.findAll('tr')
	title = soup.find('title')
	category = soup.findAll('li')
	

	print(title.text)
	print(category[2].text)
	print(tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text)


	