import pandas as pd
import io
import re
import pymysql.cursors
from converter_pdf import convert

print("Sistema Iniciado")
# ----------------------------------------------------------------------------------------



db = pymysql.connect(
  host="35.199.123.132",
  user="root",
  password="12345",
  database="matriz",
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
  )

mycursor = db.cursor()
print("Banco de Dados conectado")
# ----------------------------------------------------------------------------------------
csv = input(f"Insira o nome do arquivo csv: ")
nome_csv = f"{csv}.csv"

# ----------------------------------------------------------------------------------------

base = io.open(nome_csv, encoding='latin-1')
df_lojas = pd.DataFrame(base).to_numpy()

# ----------------------------------------------------------------------------------------

pattern_lojas_exata = r"^([0-9]{6,6})\ ([0-9.\/-]{18,18}|[ ]{18,18})\ ([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&' 0-9-,\/.?]{37,37})([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/0-9-,.]{50,50})([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/|0-9-,.]{21,21})([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/0-9-|,.]{20,20})([A-Z]{2,2})\ ([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/0-9-,.]+)"

pattern_lojas_exata2 = r"^([0-9]{6,6})([ ]{151,151})([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/0-9-,.]+)"
insert = []
insert2 = []
# ----------------------------------------------------------------------------------------
print("Loop Iniciado")
for i in df_lojas:
    a = str(i[0]).replace('?', "").replace("]", "")

    if re.findall(pattern_lojas_exata2, a):
        l2 = re.findall(pattern_lojas_exata2, a)
        linha = l2[0]
        cod_loja = int(linha[0])
        rede = linha[2]

        val2 = (cod_loja, rede)
        insert2.append(val2)


    elif re.findall(pattern_lojas_exata, a) != []:
        l = re.findall(pattern_lojas_exata, a)
        linha = l[0]
        cod_loja = int(linha[0])
        cnpj = linha[1]
        nome_loja = linha[2]
        logradouro = linha[3]
        bairro = linha[4]
        cidade = linha[5]
        uf = linha[6]
        rede = linha[7]

        val = (cod_loja, cnpj, nome_loja, logradouro, bairro, cidade, uf, rede)
        insert.append(val)

    else:
        a = ""


print("Loop Finalizado")

print(insert)
print(insert2)
print("Inserindo no banco")

sql = "INSERT INTO estabelecimentos_exata (codigo, cnpj, nome, logradouro, bairro, cidade, uf, rede) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
sql2 = "INSERT INTO estabelecimentos_exata (codigo, rede) VALUES (%s, %s)"
mycursor.executemany(sql, insert)
mycursor.executemany(sql2, insert2)
db.commit()


# ----------------------------------------------------------------------------------------

print("FIM")