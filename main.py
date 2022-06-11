import requests # informacja o użyciu bliblioteki requests
import click # informacja o użyciu bliblioteki click
from classes import bcolors # informacja o użyciu klasy bcolors z pliku classes.py
import sys # informacja o użyciu bliblioteki sys

@click.command()
@click.option('-ip', default=None, help='użycie main.py -ip <ip> // bez <>.')
def GetIP(ip): # utworzenie głównej funkcji
    """Prosty program do szukania danych po adresie ip."""
    url = f"https://ipinfo.io/{ip}/json" # deklaraca adresu zapytania GET po protokole http
    resp = requests.get(url=url) # deklaraca odpowiedzi
    data = resp.json() # informacja o formacjie odpowiedzi


    try: # obsługa błędu w razie braku danych w bazie danych serwisu ipinfo.io
        city = data['city'] # zmienna city zawiera tablicowaną odpowiedź z nazwą city
        region = data['region'] # zmienna region zawiera tablicowaną odpowiedź z nazwą region
        ip = data['ip'] # zmienna ip zawiera tablicowaną odpowiedź z nazwą adresu ip
        location = data['loc'] # zmienna location zawiera tablicowaną odpowiedź z nazwą loc
        povider = data['org'] # zmienna povider zawiera tablicowaną odpowiedź z nazwą org
        hostname = data['hostname'] # zmienna hostname zawiera tablicowaną odpowiedź z nazwą hostname'a
    except Exception as e: # jeśli brak danych przerwij operacje
        print(f"Brak {e}")
        sys.exit()


    if city or region or ip or location or povider is not None: # jeśli city lub region lub ip lub povider jest nie jest puste wypisz dane
          print(f"{bcolors.WARNING}Miasto to {city}")
          print(f"{bcolors.OKBLUE}Region jest {region}")
          print(f"{bcolors.UNDERLINE}IP jest {ip}")
          print(f"{bcolors.OKGREEN}Współżędne są {location}")
          print(f"{bcolors.HEADER}Nazwa danego hosta to {hostname}")
          print(f"{bcolors.ENDC}Dostawca połączenia to {povider}")
    else: # jeśli nie wypisz error
        print(f"{bcolors.FAIL}error")


if __name__ == '__main__': # jeśli __name__ jest __main__ wywołaj funkcje GetIP
    GetIP() # uruchomienie funkcji GetIP
