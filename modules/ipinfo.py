import requests
import sys
import argparse
from modules.colors import bcolors

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Sepcify target ip or ip range")
    options = parser.parse_args()
    return options

options = get_arguments()

def getIp(ip):
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

target = options.target
getIp(target)
