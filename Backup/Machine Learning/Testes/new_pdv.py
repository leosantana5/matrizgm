import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["Infinity_Way"]
usuarios_old = db["usuarios_old"]
mydoc = usuarios_old.find()

for x in mydoc:
    estabelecimento = x["estabelecimento"]
    for x in estabelecimento:
        cod_pdv = x["cod_pdv"]
        nome_pdv = x["nome_pdv"]
        bandeira = x["bandeira"]
        enedereco_completo_pdv = x["endereco_completo_pdv"]
        lat_pdv = x["latitude_pdv"]
        lng_pdv = x["longitude_pdv"]
        status_pdv = x["status_pdv"]
        coordenadas_pdv = (lat_pdv, lng_pdv)