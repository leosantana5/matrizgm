import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["Infinity_Way"]
usuarios_old = db["usuarios_old"]
mydoc = usuarios_old.find()

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
timestampconvertido = datetime.fromtimestamp(timestamp)
nowtime = datetime.timestamp(now)

# print(now)
# print(timestamp)
# print(timestampconvertido)
# print(nowtime)

for x in mydoc:
    cpf = x["cpf"]
    nome = x["nome_usuario"]
    endereco_completo = x["endereco_completo_usuario"]
    lat = x["latitude_usuario"]
    lng = x["longitude_usuario"]
    status = x["status_usuario"]



    usuarios = db["usuarios"]

    adicionar = {
        "cpf": cpf,
        "nome": nome,
        "endereco_completo": endereco_completo,
        "latitude": lat,
        "longitude": lng,
        "status": status,
        "data_inclusao": now,
        "data_alteracao": 0
    }
    usuarios.insert_one(adicionar)
    print(adicionar)
