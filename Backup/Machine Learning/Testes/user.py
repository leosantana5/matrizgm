import pymongo
import pandas as pd
import requests
from datetime import datetime


# API GOOGLE
api_key = 'AIzaSyAaJ4vzbbd9w7rhrYaCm7IoYhuhr8um2Eg'
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["Infinity_Way"]

usuarios = db["usuarios"]
# myquery = {"nome": "WIDSON SANTOS DE JESUS"}
# mydoc = usuarios.find(myquery)
#
# for i in mydoc:
#     print(i)
#     print("fim")


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

wb_promotor = pd.read_excel("base.xlsx", "usuarios", usecols=any)
base_promotores = pd.DataFrame(wb_promotor).to_numpy()

wb_pdvs = pd.read_excel("base.xlsx", "pdvs", usecols=any)
base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()

count = 0
for i in base_promotores:
    cpf_promotor = int(i[0])
    nome_promotor = str(i[1])
    perfil_promotor = str(i[2])
    sexo_promotor = str(i[3])
    contato_promotor = str(i[4])
    status_promotor = str(i[5])
    logradouro_promotor = str(i[6])
    numero_promotor = str(i[7])
    bairro_promotor = str(i[8])
    cidade_promotor = str(i[9])
    uf_promotor = str(i[10])
    cep_promotor = str(i[11])
    inicio_jornada_promotor = str(i[14])
    fim_jornada_promotor = str(i[15])
    pausa_jornada_promotor = str(i[16])
    meio_transporte_promotor = str(i[17])
    jornada_semana_promotor = str(i[18])
    descanso_semanal_promotor = str(i[19])
    cpf_supervisor = str(i[20])
    nome_supervisor = str(i[21])
    endereco_completo_promotor = f'{logradouro_promotor},' \
                        f' {numero_promotor}, ' \
                        f'{bairro_promotor}, ' \
                        f'{cidade_promotor}, ' \
                        f'{uf_promotor}, ' \
                        f'cep {cep_promotor}'


    usuarios = db["usuarios"]
    myquery = {"nome": str(nome_promotor)}
    mydoc = usuarios.find(myquery)



    results = list(mydoc)

    if results != []:
        myquery = {"nome": str(nome_promotor)}
        mydoc = usuarios.find(myquery)
        for i in mydoc:
            cpf = i['cpf']
            nome = i['nome']
            perfil = i['perfil']
            endereco_completo = i['endereco_completo']
            latitude = i['latitude']
            longitude = i['longitude']
            status = i['status']
            data_inclusao = i['data_inclusao']
            data_alteracao = i['data_alteracao']
            now = datetime.now()
            now = str(datetime.timestamp(now))

            myquery = {"data_alteracao": data_alteracao}
            newvalues = {"$set": {"data_alteracao": ""}}
            usuarios.update_one(myquery, newvalues)

            # atualização do banco

            print(f'Promotor {nome} - já cadastrado no banco')

    else:

        adicionar_usuario = {
            "cpf": str(cpf_promotor),
            "nome": nome_promotor,
            "perfil": perfil_promotor,
            "endereco_completo": endereco_completo_promotor,
            "latitude": get_lat(endereco_completo_promotor),
            "longitude": get_lng(endereco_completo_promotor),
            "status": status_promotor,
            "data_inclusao": now,
            "data_alteracao": now
        }
        usuarios.insert_one(adicionar_usuario)
        count += 1



        print(count, adicionar_usuario)




