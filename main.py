from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
#import xlsxwriter

BASE = os.getcwd()
r = requests.get("https://www.iqair.com/world-air-quality-ranking")

soup = BeautifulSoup(r.text, 'html.parser')

cities = []

table = soup.find("table", attrs={"class": "mb30"})
for row in table.findAll("tr")[1:]:
    columns = row.findAll("td")
    stats = {
        "city": columns[2].text.split(", ")[0],
        "state": columns[2].text.split(", ")[1],
        "aqi": columns[3].text
    }
    cities.append(stats)


df = pd.DataFrame(cities)
writer = pd.ExcelWriter(BASE + '\\state.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet 1', index=False)
writer.save()