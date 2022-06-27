#/usr/bin/python

import requests
import sys
import typer
from modules.colors import bcolors

app = typer.Typer()

@app.command("getIp")
def getIp(
    ip: str = typer.Option(..., help="ip.")):
    url = f"https://ipinfo.io/{ip}/json"
    resp = requests.get(url=url)
    data = resp.json()

    try:
        city = data['city']
        region = data['region']
        ip = data['ip']
        location = data['loc']
        povider = data['org']
        hostname = data['hostname']
    except Exception as e:
        print(f"Brak {e}")
        sys.exit()

    if city or region or ip or location or povider is not None:
          print(f"{bcolors.WARNING}Miasto to {city}")
          print(f"{bcolors.OKBLUE}Region jest {region}")
          print(f"{bcolors.UNDERLINE}IP jest {ip}")
          print(f"{bcolors.OKGREEN}Współżędne są {location}")
          print(f"{bcolors.HEADER}Nazwa danego hosta to {hostname}")
          print(f"{bcolors.ENDC}Dostawca połączenia to {povider}")
    else:
        print(f"{bcolors.FAIL}error")

app()
