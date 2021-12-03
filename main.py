from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

BASE = os.getcwd()

r = requests.get("https://www.iqair.com/world-air-quality-ranking")

soup = BeautifulSoup(r.text, 'html.parser')

cities = []

table = soup.find("table", attrs={"class": "mb30"})
for row in table.findAll("tr")[1:]:
    columns = row.findAll("td")
    city, state = columns[2].text.split(",")[0].strip(), columns[2].text.split(",")[1].strip()
    stats = {
        "city": city,
        "state": state,
        "aqi": columns[3].text
    }
    cities.append(stats)


df = pd.DataFrame(cities)

writer = pd.ExcelWriter(BASE + '\\air_quality.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1', index=False)

writer.save()

