import requests
import pandas as pd


destino = "Rua Professor Eldemar Alves de Oliveira, 176"
origem = "Rua Eduardo Chq   weraves, 183"
# API GOOGLE
api_key = 'AIzaSyAaJ4vzbbd9w7rhrYaCm7IoYhuhr8um2Eg'

def get_lat(endereco):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={origem}&key={api_key}'
    r = requests.get(url).json()
    status = r["status"]
    results = r["results"]

    if status == "OK":
        for a in results:
            geometry = a["geometry"]
            location = geometry["location"]
            lat = location["lat"]
            lng = location["lng"]

    else:
        lat = ""
        lng = ""
    return print(lat, lng)

print(get_lat(destino), get_lat(origem))






