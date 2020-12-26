import pandas as pd
import os.path
import pymysql.cursors

# ----------------------------------------------------------------------------------------

db = pymysql.connect(
  host="35.199.123.132",
  user="root",
  password="12345",
  database="matriz",
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
  )

# ----------------------------------------------------------------------------------------

save_path = 'M:/2 - PDV Action/'
file_estabelecimentos = 'Estabelecimentos PDV+Exata.xlsx'
path_estabelecimentos = os.path.join(save_path, file_estabelecimentos)



def ler_estabelecimentos():
    count_pdv = []
    wb_pdvs = pd.read_excel(path_estabelecimentos, "Sheet1", usecols=any)
    print("Leitura do arquivo estabelecimentos, concluída")
    base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()
    print("arquivo convertido em Data Frame")
    insert1 = []
    count_pdv = 0
    for i in base_pdvs:
        # print(i)
        codigorede = str(i[1])
        rede = str(i[2])
        codigobandeira = str(i[3])
        bandeira = str(i[4])
        codigo = str(i[5])
        nome = str(i[6])
        cnpj = str(i[7])
        cep = str(i[8])
        logradouro = str(i[9])
        numero = str(i[10])
        complemento = str(i[11])
        bairro = str(i[12])
        cidade = str(i[13])
        uf = str(i[14])
        latitude = str(i[15])
        longitude = str(i[16])
        regional = str(i[17])
        zona = str(i[18])
        status = str(i[19])
        cod_exata = str(i[20]) or None
        endereco_completo = f"{logradouro},{numero} - {complemento} - {bairro} - {cidade} - {uf} - {cep}"


        val = (codigo, nome, bandeira, cnpj, logradouro, numero, bairro, cidade, uf, cep, endereco_completo, latitude, longitude, regional, zona, status, cod_exata)

        insert1.append(val)

        count_pdv += 1

        print(count_pdv)

    sql = "INSERT INTO estabelecimentos (cod_loja, nome, bandeira, cnpj, logradouro, numero_logradouro, bairro, cidade, uf, cep, endereco_completo, latitude, longitude, regional, zona, status, cod_loja_exata) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor = db.cursor()
    mycursor.executemany(sql, insert1)
    db.commit()
    print(mycursor.rowcount, "was inserted.")

ler_estabelecimentos()