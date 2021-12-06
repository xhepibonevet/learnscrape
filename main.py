import typer
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import xlsxwriter
from notify import notification


app = typer.Typer()
BASE = os.getcwd()

def retrieve_cities_list():
    r = requests.get("https://www.iqair.com/world-air-quality-ranking")

    soup = BeautifulSoup(r.text, 'html.parser')

    cities = []

    table = soup.find("table", attrs={"class": "mb30"})
    for row in table.findAll("tr")[1:]:
        columns = row.findAll("td")
        stats = {
            "city": columns[2].text.split(",")[0].strip(),
            "state": columns[2].text.split(", ")[1],
            "aqi": columns[3].text
        }
        cities.append(stats)
        return cities

def write_xl():
    df = pd.DataFrame(retrieve_cities_list())
    writer = pd.ExcelWriter(BASE + '\\state.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet 1', index=False)
    writer.save()

def notify(qyteti):
    for city in retrieve_cities_list():
        if qyteti == city.get('city'):
            if int(city.get('aqi')) >= 100:
                notification(qyteti)

if __name__ == "__main__":
    app()