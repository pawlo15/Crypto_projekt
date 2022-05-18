import sys
import requests
from bs4 import BeautifulSoup

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
liczba = float(tempStr)
# jeżeli chcemy wyświetlić nazwę waluty i jej wartość

# waluta = strona.p
# waluta = str(waluta)
# waluta = waluta[waluta.find('>')+1:]
# waluta = waluta[:waluta.find('<')]
# print('{0} {1} PLN'.format(waluta, liczba))
