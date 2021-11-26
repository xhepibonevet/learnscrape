from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.scrapethissite.com/faq/")

soup = BeautifulSoup(r.text, 'html.parser')

