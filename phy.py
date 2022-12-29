#extract the data from physics column from nobel file
#
import csv
import re
import sys
import os
import requests
from bs4 import BeautifulSoup
import csv
url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"class": "wikitable sortable"})
rows = table.find_all("tr")
with open("nobel.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        writer.writerow(cols)