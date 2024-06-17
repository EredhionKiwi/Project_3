"""
projekt_3

autor: Jirka Hajek

"""

import requests
from bs4 import BeautifulSoup
import cv2
import csv


adresa = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102"
adresa_prefix = "https://www.volby.cz/pls/ps2017nss/"

def findin_link(adresa):
    response = requests.get(adresa)
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')

    links = []
    for row in rows:
        cells = row.find_all('td', class_='cislo')
        for anchor in row.find_all('a'):
            links.append(anchor['href'])
            for link in links:
                global stranka
                stranka = [adresa_prefix + link]
                print (stranka)




findin_link(adresa)


def krok2():
    for x in stranka:
        print(x)
        
        response = requests.get(x)
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')

        for row in rows:
            cells = row.find_all('td', class_='cislo')
            name = row.find_all('td', class_='overflow_name')
            print(cells, name)
        


krok2()
