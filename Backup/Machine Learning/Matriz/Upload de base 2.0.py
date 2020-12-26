import pymysql.cursors
import pymongo
from datetime import datetime

db = pymysql.connect(
  host="35.199.123.132",
  user="admin",
  password="12345",
  database="matriz",
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
  )

sql = "INSERT INTO estabelecimentos (codigo, nome, bandeira, cnpj, cep, logradouro, numero, complemento, bairro, cidade, uf, latitude, longitude, regional, zona, status, endereco_completo, data_inclusao, data_alteracao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


mongonline = pymongo.MongoClient("mongodb+srv://admin:matriz@leonardosantana.qgnlf.mongodb.net/bases_pdvaction?retryWrites=true&w=majority")
dbmatriz = mongonline["bases_pdvaction"]
col_pdv = dbmatriz["pdv_pdvaction"]

for i in col_pdv.find():
    codigo = i["codigo"]
    nome = i["nome"]
    bandeira = i["bandeira"]
    cnpj = i["cnpj"]
    cep = i["cep"]
    logradouro = i["logradouro"]
    numero = i["numero"]
    complemento = ["complemento"]
    bairro = i["bairro"]
    cidade = i["cidade"]
    uf = i["uf"]
    latitude = i["latitude"]
    longitude = i["longitude"]
    regional = i["regional"]
    zona = i["zona"]
    status = i["status"]
    endereco_completo = i["endereco_completo"]
    data_inclusao = datetime.now()
    data_alteracao = datetime.now()
    val = (codigo, nome, bandeira, cnpj, cep, logradouro, numero, complemento, bairro, cidade, uf, latitude, longitude, regional, zona, status, endereco_completo, data_inclusao, data_alteracao)
    select = f"SELECT * FROM estabelecimentos WHERE codigo ='{codigo}'"

    mycursor = db.cursor()

    mycursor.execute(select)

    # db.commit()

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # print(mycursor.rowcount, codigo)





