import pymysql.cursors
import pymongo


mongonline = pymongo.MongoClient("mongodb+srv://admin:matriz@leonardosantana.qgnlf.mongodb.net/bases_pdvaction?retryWrites=true&w=majority")
dbmatriz = mongonline["bases_pdvaction"]
col_pdvs = dbmatriz["pdv_pdvaction"]


db = pymysql.connect(
  host="35.199.123.132",
  user="admin",
  password="12345",
  database="matriz",
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
  )
mydb = db.cursor()

# mydb.execute("CREATE DATABASE MATRIZ")

mydb.execute("CREATE TABLE estabelecimentos (id INT AUTO_INCREMENT PRIMARY KEY,codigo INTEGER(8),nome VARCHAR(80),bandeira VARCHAR(255),cnpj VARCHAR(255),cep VARCHAR(255),logradouro VARCHAR(255),numero VARCHAR(255),complemento VARCHAR(255),bairro VARCHAR(255),cidade VARCHAR(255),uf VARCHAR(255),latitude VARCHAR(255),longitude VARCHAR(255),regional VARCHAR(255),zona VARCHAR(255),status BOOL,endereco_completo VARCHAR(255),data_inclusao DATETIME,data_alteracao DATETIME)")



