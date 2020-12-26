import pymysql.cursors

db = pymysql.connect(
  host="127.0.0.1",
  user="usertest",
  password="usertest",
  database="matriz",
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
  )

codloja = 375
nome = "13 - AKKI ATACADISTA - JOAO DIAS"



mydb = db.cursor()
insert = f'INSERT INTO ESTABELECIMENTOS (Cod, Nome) VALUES (%s, %s)'
val = (codloja, nome)

mydb.execute(insert, val)


print(mydb.rowcount, "record inserted.")

# mydb.execute("CREATE DATABASE MATRIZ")
#
# mydb.execute("DROP TABLE ESTABELECIMENTOS")
#
# mydb.execute("ALTER TABLE matriz.estabelecimentos MODIFY COLUMN Status BOOL DEFAULT NULL NULL")

# mydb.execute("CREATE TABLE ESTABELECIMENTOS (id INT AUTO_INCREMENT PRIMARY KEY, Cod INTEGER(8), Nome VARCHAR(80), Bandeira VARCHAR(255),Logradouro VARCHAR(255),Numero_Logradouro VARCHAR(255), Complemento_Logradouro VARCHAR(255), Bairro_Logradouro VARCHAR(255), Cidade_Logradouro VARCHAR(255), UF_Logradouro VARCHAR(255), CEP_Logradouro VARCHAR(255), CNPJ VARCHAR(255), Latitude VARCHAR(255), Longitude VARCHAR(255), Regional VARCHAR(255), Status BOOL)")

