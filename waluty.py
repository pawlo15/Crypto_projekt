import requests
import csv
import os
from bs4 import BeautifulSoup
from datetime import datetime

strony = ['https://e-kursy-walut.pl/kurs-euro/','https://e-kursy-walut.pl/kurs-dolara/','https://e-kursy-walut.pl/kurs-franka/','https://e-kursy-walut.pl/kurs-funta/']
now = datetime.now()

def pobierz_walute(web):
    url_page = web
    page = requests.get(url_page)
    strona = BeautifulSoup(page.content, 'html.parser')
    kurs_waluty = strona.find_all(itemprop='price')
    tempStr = str(kurs_waluty)
    tempStr = tempStr[tempStr.find('\"') + 1:]
    tempStr = tempStr[:tempStr.find('\"')]
    waluta = strona.p                             # jeżeli chcemy wyświetlić nazwę waluty i jej wartość
    waluta = str(waluta)                          #
    waluta = waluta[waluta.find('>')+1:]          #
    waluta = waluta[:waluta.find('<')]            #
    kurs_waluty = waluta[waluta.find('(')+1:]     #
    kurs_waluty = kurs_waluty[:3]                 #
    print('{0} {1} PLN'.format(waluta, tempStr))  # wypisujemy walutę 

    struct = {'price': tempStr,                  # przypisanie wartości
              'waluta':kurs_waluty,              # przypisanie waluty
              'time': now.strftime("%H:%M:%S"),  # przypisanie godziny
              'data': now.strftime("%d/%m/%Y")}  # przypisanie daty
    return struct

if os.path.exists('plik.csv'):
     with open('plik.csv', 'a', encoding='utf-8') as CSVfile:
        fieldnames = ['price', 'waluta', 'time', 'data']
        csvwriter = csv.DictWriter(CSVfile, fieldnames=fieldnames)
        for web in strony:
            csvwriter.writerow(pobierz_walute(web)) # zapis do pliku waluty (w pętli)
else:
    with open('plik.csv', 'w', encoding='utf-8') as CSVfile:
        fieldnames = ['price', 'waluta', 'time', 'data']
        csvwriter = csv.DictWriter(CSVfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        for web in strony:
            csvwriter.writerow(pobierz_walute(web)) # zapis do pliku waluty (w pętli)

try:
    CSVfile.close()
except IOError:
    print("Nie udało się zamknąć pliku.")
else:
    print("Zamknięto plik")
