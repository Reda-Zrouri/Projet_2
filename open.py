import requests 
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
reponse = requests.get (url)
if reponse.ok: 
	soup = BeautifulSoup(reponse.text, 'lxml')
	titre = soup.find('article', {'class': 'product_page'}).find('h1')
	production = soup.find('table')
	print("titre: " + titre.text + " Production Information: " + production.text)
	
