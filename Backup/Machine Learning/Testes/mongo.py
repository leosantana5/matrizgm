import pymongo
from datetime import datetime


now = datetime.now()
timestamp = now.timestamp()
dia = now.day
mes = now.month
ano = now.year
hora = now.hour
minuto = now.minute
mes = now.month
segundo = now.second
diadehj = f'{dia}/{mes}/{ano} {hora}:{minuto}'

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["Infinity_Way"]

def cadastrar_distancia(cpf,nome_usuario,endereco_completo_usuario,coordenadas_usuario, status_usuario,
                       cod_pdv, nome_pdv, bandeira, endereco_completo_pdv, coordenadas_pdv, status_pdv,
                       distancia):

    adicionar = {
        "origem": {
            "cpf": cpf,
            "nome_usuario": nome_usuario,
            "endereco_completo_usuario": endereco_completo_usuario,
            "coordenadas_usuario": coordenadas_usuario,
            "status_usuario": status_usuario

        },
        "destino": {
            "cod_pdv": cod_pdv,
            "nome_pdv": nome_pdv,
            "bandeira": bandeira,
            "endereco_completo_pdv": endereco_completo_pdv,
            "coodenadas_pdv": coordenadas_pdv,
            "status_pdv": status_pdv
        },
        "percurso":  distancia

    }
    usuario_vs_estabelecimentos = db["usuario_vs_estabelecimentos"]
    usuario_vs_estabelecimentos.insert_one(adicionar)



def cadastrar_usuario(cpf, nome_usuario, endereco_completo_usuario, latitude_usuario, longitute_usuario,
                       status_usuario):

    usuarios = db["usuarios"]
    adicionar = {
            "cpf": cpf,
            "nome": nome_usuario,
            "endereco_completo": endereco_completo_usuario,
            "latitude": latitude_usuario,
            "longitute": longitute_usuario,
            "status": status_usuario,
            "data_inclusao":timestamp,
            "data_processada":timestamp
        }

    usuarios.insert_one(adicionar)
    return print(f'{cpf} / {nome_usuario} / {latitude_usuario}-{longitute_usuario}')

def cadastrar_estabelecimento(cod_pdv, nome_pdv, bandeira, endereco_completo_pdv, latitude_pdv, longitude_pdv, status_pdv):
    pdvs = db["pdvs"]

    adicionar = {
            "cod_pdv": cod_pdv,
            "nome_pdv": nome_pdv,
            "bandeira": bandeira,
            "endereco_completo_pdv": endereco_completo_pdv,
            "latitude_pdv": latitude_pdv,
            "longitude_pdv": longitude_pdv,
            "status_pdv":status_pdv
    }
    pdvs.insert_one(adicionar)
    return print(f'{nome_pdv} / lat({latitude_pdv})lng({longitude_pdv})')


def query_usuario(nome):
    usuarios = db["usuarios"]
    myquery = {"nome_usuario": str(nome)}
    mydoc = usuarios.find(myquery)
    for i in mydoc:
        print(i)



query_usuario("ZILTON FERNANDES SANTOS")

def query_estabelecimento (cod_pdv):

    pdv = db["pdv"]
    myquery = {"pdv.cod": str(cod_pdv)}
    mydoc = pdv.find(myquery)
    print(mydoc)
    for x in mydoc:
        cod_pdv = x["cod_pdv"]
        nome_pdv = x["nome_pdv"]
        bandeira = x["bandeira"]
        enedereco_completo_pdv = x["endereco_completo_pdv"]
        lat_pdv = x["latitude_pdv"]
        lng_pdv = x["longitude_pdv"]
        status_pdv = x["status_pdv"]
        coordenadas_pdv = (lat_pdv, lng_pdv)
        print(x)

        return coordenadas_pdv



