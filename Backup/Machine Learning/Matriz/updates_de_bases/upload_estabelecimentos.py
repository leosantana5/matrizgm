from win10toast import ToastNotifier
import requests
import pandas as pd
import os.path
import pymysql.cursors
from threading import Thread

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

def regiao (uf):
  if uf == "DF" or uf == "GO" or  uf == "MT" or  uf =="MS":
    return ("Centro-Oeste")
  elif uf == "AL" or uf == "BA" or uf == "CE" or uf =="MA" or uf == "PB" or uf == "PE" or uf =="PI" or uf == "RN" or uf =="SE":
    return ("Nordeste")
  elif uf == "AC" or uf == "AP" or uf == "AM" or uf =="PA" or uf == "RO" or uf == "RR" or uf =="TO":
    return ("Norte")
  elif uf == "SP":
    return ("Sudeste 1")
  elif uf == "MG":
    return ("Sudeste 3")
  elif uf == "ES" or uf == "RJ":
    return ("Sudeste 2")
  elif uf == "PR" or uf == "RS" or uf == "SC":
    return ("Sul")

# ----------------------------------------------------------------------------------------

save_path = 'M:/2 - PDV Action/'

print("Sistema Iniciado")
# ----------------------------------------------------------------------------------------

url_lojas = "http://api.grupogmpromo.pdvaction.com.br/api/estabelecimento/exportarxlsx"
file_estabelecimentos = 'Estabelecimentos PDV.xlsx'
path_estabelecimentos = os.path.join(save_path, file_estabelecimentos)


t = ToastNotifier()

# ----------------------------------------------------------------------------------------


p_estabelecimentos = {
    "Exportar": False,
    "OrderBy": "Codigo",
    "OrderType": "desc",
    "idUsuarioRequest": "5d42c679bc25f6225463fd93"}


# ___________________________________________________________________________________

def baixar_estabelecimentos():
    t.show_toast("Estabelecimentos","Começou a baixar estabelecimentos")
    print("resposta web concluída")
    print("salvando arquivo na pasta")
    res_estabelecimentos = requests.post(url_lojas, json=p_estabelecimentos)
    with open(path_estabelecimentos, 'wb') as output:
        output.write(res_estabelecimentos.content)


# ___________________________________________________________________________________
print("")
# baixar_estabelecimentos()
print("Base de estabelecimentos baixada")



# LEITURA DAS BASES  ------------------------------

def ler_pdv():
    wb_pdvs = pd.read_excel(path_estabelecimentos, "Sheet1", usecols=any)
    base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()
    insertloja = []
    df1 = insertloja.where(pd.notnull(insertloja), None)
    count_nova_loja = 0
    for loja in base_pdvs:
        datainclusaoregistro = loja[0]
        codigorede = loja[1]
        rede = loja[2]
        codigobandeira = loja[3]
        bandeira = loja[4]
        codigo = loja[5]
        nome = loja[6]
        cnpj = loja[7]
        cep = loja[8]
        logradouro = loja[9]
        numero = loja[10]
        complemento = loja[11]
        bairro = loja[12]
        cidade = loja[13]
        uf = loja[14]
        latitude = loja[15]
        longitude = loja[16]
        regional = loja[17]
        zona = loja[18]
        status = loja[19]
        codigocliente = loja[20]
        endereco_completo = f"{logradouro}, {numero}, - {bairro} - {cidade} - {uf} - {cep}"

        mycursor.execute(f"SELECT * FROM estabelecimentos WHERE cod_loja = {codigo}")
        myresult = mycursor.fetchall()

        if myresult == ():
            val =(codigo, bandeira, nome, logradouro, numero, bairro, cidade, uf, cep, endereco_completo, cnpj, latitude, longitude, regiao(uf), zona, status, datainclusaoregistro)
            sql = "INSERT INTO matriz_pdv (cod_loja, bandeira, nome, logradouro, numero_logradouro, bairro, cidade, uf, cep, endereco_completo, cnpj, latitude, longitude,regional, zona, status, data_inclusao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insertloja.append(val)
            count_nova_loja += 1



            print(f"{codigo} - NÂO ENCONTRADO")
        else:
            for x in myresult:
                print(x["cod_loja"])
    mycursor.executemany(sql, df1)
    print(mycursor.rowcount, "was inserted.")
print("")

# ______________

thread = Thread(target = ler_pdv())
thread.start()


print("FIM")
