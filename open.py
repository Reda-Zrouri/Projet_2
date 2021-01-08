#import module

import requests 
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
img = "http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"


with open('projet2.csv', 'w') as outf:
	reponse = requests.get(url)
	if reponse.ok: 
		soup = BeautifulSoup(reponse.text, 'lxml')
		tds = soup.findAll('tr')
		title = soup.find('title')
		category = soup.findAll('li')

		
		print(url)
		print(title.text)
		print(category[2].text)
		print(tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text)
		print(img)
		outf.write(url + ',' + title.text + ',' + category[2].text + ',' + tds[0].text + ',' + tds[1].text + ',' + tds[3].text + ',' + tds[4].text + ',' + tds[5].text + ',' + tds[6].text + ',' + img)