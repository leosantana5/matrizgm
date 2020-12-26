# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE mydatabase")


# def regiao (uf):
#   if uf == "DF" or uf == "GO" or  uf == "MT" or  uf =="MS":
#     return ("Centro-Oeste")
#   elif uf == "AL" or uf == "BA" or uf == "CE" or uf =="MA" or uf == "PB" or uf == "PE" or uf =="PI" or uf == "RN" or uf =="SE":
#     return ("Nordeste")
#   elif uf == "AC" or uf == "AP" or uf == "AM" or uf =="PA" or uf == "RO" or uf == "RR" or uf =="TO":
#     return ("Norte")
#   elif uf == "SP":
#     return ("Sudeste 1")
#   elif uf == "MG":
#     return ("Sudeste 3")
#   elif uf == "ES" or uf == "RJ":
#     return ("Sudeste 2")
#   elif uf == "PR" or uf == "RS" or uf == "SC":
#     return ("Sul")
#
# print(regiao("MG"))


import pymongo
import pandas as pd
from datetime import datetime
import requests
import os

wb_pdvs = pd.read_excel("bases pdv/estabelecimentos_pdvaction.xlsx", "Sheet1", usecols=any)
base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()

def consultar_cnpj(cnpj):
    url = f"https://consulta-cnpj-gratis.p.rapidapi.com/companies/{cnpj}"

    headers = {
        'x-rapidapi-key': "72c3596d5dmshd562d75715d4ae3p1fd0ddjsn74fb28b2d5cd",
        'x-rapidapi-host': "consulta-cnpj-gratis.p.rapidapi.com"
        }

    r = requests.request("GET", url, headers=headers).json()
    razao_social = r['name']
    fantasia = r['alias']
    tipe = r['type']
    registration = r['registration']
    status = registration['status']
    endereco_completo = r['address']
    rua = endereco_completo['street']
    numero = endereco_completo['number']
    bairro = endereco_completo['neighborhood']
    cidade = endereco_completo['city']
    uf = endereco_completo['state']
    cidade_ibge = endereco_completo['city_ibge']
    uf_ibge = endereco_completo['state_ibge']
    cep = endereco_completo['zip']

    jailson = {
        "razao_social":razao_social,
        "fantasia":fantasia,
        "tipo":tipe,
        "status":status,
        "endereco_completo": f'{rua}, {numero}, {bairro}, {cidade},{uf}, {cep}',
        "rua": rua,
        "numero":numero,
        "bairro":bairro,
        "cidade":cidade,
        "up":uf,
        "cep":cep,
        "ibge_cidade":cidade_ibge,
        "ibge_uf":uf_ibge
    }

    print(r)
    print(razao_social)
    # print(fantasia)
    # print(status)
    # print(endereco_completo)
    # print(rua)
    # print(numero)
    # print(bairro)
    # print(cidade)
    # print(uf)
    # print(cep)
    # print(cidade_ibge)
    # print(uf_ibge)
    print(jailson)

consultar_cnpj("12539517000647")
for i in base_pdvs:
    datainclusaoregistro = str(i[0])
    codigorede = int(i[1])
    rede = str(i[2])
    codigobandeira = int(i[3])
    bandeira = str(i[4])
    codigo = int(i[5])
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
    endereco_completo_pdv = f'{logradouro},' \
                        f' {numero}, ' \
                        f'{bairro}, ' \
                        f'{cidade}, ' \
                        f'{uf}, ' \
                        f'cep {cep}'

    if status == "Ativo":
        try:
            consultar_cnpj(cnpj)
        except:
            print(nome, cnpj)