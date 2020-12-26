import pandas as pd
import requests
import pymongo

# API GOOGLE
api_key = 'AIzaSyAaJ4vzbbd9w7rhrYaCm7IoYhuhr8um2Eg'


def get_lat(endereco):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={api_key}'
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
    return lat


def get_lng(endereco):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={api_key}'
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
    return lng


def cadastrar_no_banco(cod_pdv, nome_pdv, bandeira, endereco_completo_pdv, latitude_pdv, longitude_pdv, status_pdv):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client["Infinity_Way"]
    estabelecimentos = db["estabelecimentos"]

    adicionar = {
        "estabelecimento": [{
            "cod_pdv": cod_pdv,
            "nome_pdv": nome_pdv,
            "bandeira": bandeira,
            "endereco_completo_pdv": endereco_completo_pdv,
            "latitude_pdv": latitude_pdv,
            "longitude_pdv": longitude_pdv,
            "status_pdv":status_pdv
        }]
    }
    estabelecimentos.insert_one(adicionar)
    return print(f'{nome_pdv} / lat({latitude_pdv})lng({longitude_pdv})')



wb_promotor = pd.read_excel("base.xlsx", "usuarios", usecols=any)
base_promotores = pd.DataFrame(wb_promotor).to_numpy()
wb_pdvs = pd.read_excel("base.xlsx", "pdvs", usecols=any)
base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()

for i in base_pdvs:
    cod_pdv = str(i[0])
    nome_pdv = str(i[1])
    bandeira_pdv = str(i[2])
    logradouro_pdv = str(i[3])
    numero_pdv = str(i[4])
    bairro_pdv = str(i[5])
    cidade_pdv = str(i[6])
    uf_pdv = str(i[7])
    cep_pdv = str(i[8])
    status_pdv = str(i[11])
    endereco_completo_pdv = f'{logradouro_pdv},{numero_pdv},{bairro_pdv},{cidade_pdv},{uf_pdv},{cep_pdv}'

    cadastrar_no_banco(
        cod_pdv=cod_pdv,
        nome_pdv=nome_pdv,
        bandeira=bandeira_pdv,
        endereco_completo_pdv=endereco_completo_pdv,
        latitude_pdv=get_lat(endereco_completo_pdv),
        longitude_pdv=get_lng(endereco_completo_pdv),
        status_pdv=status_pdv
    )