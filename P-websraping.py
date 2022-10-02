from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page=requests.get(START_URL)
soup=bs4(page.text,'html.parser')
start_table=soup.find('table')

temp_list=[]
table_rows=start_table.find_all('tr')
for tr in table_rows:
    row=[i.text.r strip()for i in td]
    temp_list.append(row)