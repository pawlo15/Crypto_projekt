import sys
import requests
import csv
import os
from bs4 import BeautifulSoup
from datetime import datetime

if len(sys.argv) > 1:
    url_page = sys.argv[1] #str(sys.argv) # argumentem jest link do strony
else:
    url_page = 'https://e-kursy-walut.pl/kurs-szekla-izraelskiego/'
page = requests.get(url_page)
strona = BeautifulSoup(page.content, 'html.parser')
kurs_waluty = strona.find_all(itemprop='price')
tempStr = str(kurs_waluty)
tempStr = tempStr[tempStr.find('\"') + 1:]
tempStr = tempStr[:tempStr.find('\"')]

# jeżeli chcemy wyświetlić nazwę waluty i jej wartość
#waluta = strona.p
#waluta = str(waluta)
#waluta = waluta[waluta.find('>')+1:]
#waluta = waluta[:waluta.find('<')]
#print('{0} {1} PLN'.format(waluta, liczba))

now = datetime.now()                        # pobranie daty i godziny
date_time = now.strftime("%H:%M:%S %d/%m/%Y")

struct = {'price': tempStr,                 # zapis wartości
          'time': now.strftime("%H:%M:%S"), # zapis godziny
          'data': now.strftime("%d/%m/%Y")} # zapis daty

if os.path.exists('plik.csv'):              # dopisujemy do plik.csv jeśli istnieje
    with open('plik.csv', 'a', encoding='utf-8') as CSVfile:
        fieldnames = ['price', 'time', 'data']
        csvwriter = csv.DictWriter(CSVfile, fieldnames=fieldnames)
        csvwriter.writerow(struct)
else:                                       # tworzymy plik.csv jeżeli nie istaniał
    with open('plik.csv', 'w', encoding='utf-8') as CSVfile:
        fieldnames = ['price', 'time', 'data']
        csvwriter = csv.DictWriter(CSVfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerow(struct)

CSVfile.close()
