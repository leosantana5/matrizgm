import pymongo
import pandas as pd
from datetime import datetime
import requests
import os
import pymysql.cursors

clear = lambda: os.system('cls')
mongonline = pymongo.MongoClient("mongodb+srv://admin:matriz@leonardosantana.qgnlf.mongodb.net/bases_pdvaction?retryWrites=true&w=majority")
mongolocal = pymongo.MongoClient('mongodb://localhost:27017/')
dbmatriz = mongonline["bases_pdvaction"]
ativos = dbmatriz["clientes_ativos"]
encerrados = dbmatriz["clientes_encerrados"]

# API GOOGLE         ------------------------------
api_key = 'AIzaSyAaJ4vzbbd9w7rhrYaCm7IoYhuhr8um2Eg'

# FUNÇÕES            ------------------------------

def get_lat(endereco):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={api_key}'
    r = requests.get(url).json()
    status = r["status"]
    results = r["results"]

    if status == "OK":
        for a in results:
            geometry = a["geometry"]
            location = geometry["location"]
            formatted_address = a["formatted_address"]
            lat = location["lat"]
            lng = location["lng"]

    else:
        lat = ""
        lng = ""
    return lat

def get_lng(endereco):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={api_key}'
    r = requests.get(url).json()
    status = r["status"]
    results = r["results"]

    if status == "OK":
        for a in results:
            geometry = a["geometry"]
            location = geometry["location"]
            lat = location["lat"]
            lng = location["lng"]

    else:
        lat = ""
        lng = ""
    return lng

def consultar_endereco(cep):
    cep = str(cep)
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={cep}&key={api_key}'
    r = requests.get(url).json()
    status = r["status"]
    results = r["results"]

    if status == "OK":
        for a in results:
            geometry = a["geometry"]
            location = geometry["location"]
            endereco = a["formatted_address"]
            lat = location["lat"]
            lng = location["lng"]

    else:
        lat = ""
        lng = ""
        endereco = ""
    return endereco

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

# LEITURA DAS BASES  ------------------------------

wb_usuarios = pd.read_excel("bases pdv/usuarios_pdvaction.xlsx", "Sheet1", usecols=any)
base_usuarios = pd.DataFrame(wb_usuarios).to_numpy()

wb_pdvs = pd.read_excel("bases pdv/estabelecimentos_pdvaction.xlsx", "Sheet1", usecols=any)
base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()

# CONTADOR DE DADOS  ------------------------------
count_usuarios_jacadastrados = 0
count_usuarios_cadastrados = 0
count_pdvs_jacadastrados = 0
count_pdvs_cadastrados = 0

for i in base_usuarios:

    codigo = str(i[0])
    nome = str(i[1])
    empresa = str(i[2])
    login = str(i[3])
    email = str(i[4])
    idperfilacessosistema = str(i[5])
    cep = str(i[6])
    logradouro = str(i[7])
    numero = str(i[8])
    complemento = str(i[9])
    bairro = str(i[10])
    cidade = str(i[11])
    uf = str(i[12])
    latitude = str(i[13])
    longitude = str(i[14])
    telefone = str(i[15])
    datanascimento = str(i[16])
    rg = str(i[17])
    orgaoemissor = str(i[18])
    cpf = str(i[19])
    banco = str(i[20])
    agencia = str(i[21])
    conta = str(i[22])
    tipoconta = str(i[23])
    ctpsnumero = str(i[24])
    ctpsserie = str(i[25])
    ctpsestado = str(i[26])
    admissao = str(i[27])
    desligamento = str(i[28])
    pis = str(i[29])
    custooperacional = str(i[30])
    nacionalidade = str(i[31])
    estadocivil = str(i[32])
    sexo = str(i[33])
    status = str(i[34])
    superior = str(i[35])
    datainclusao = str(i[36])
    dataalteracao = str(i[37])
    statusexclusao = str(i[38])
    endereco_completo_promotor = f'{logradouro},' \
                                 f' {numero}, ' \
                                 f'{bairro}, ' \
                                 f'{cidade}, ' \
                                 f'{uf}, ' \
                                 f'cep {cep}'


    if statusexclusao != "Inativo":
        if status != "Inativo":
            if idperfilacessosistema != "cliente" and \
                    idperfilacessosistema != "retencao" and \
                    idperfilacessosistema != "semroteiro":
                if cpf != "nan":

                    # verificar se o promotor(CPF) já está cadastrado e retornar o resultado
                    usuarios = dbmatriz["usuarios_pdvaction"]
                    mq = {"cpf": str(int(cpf))}
                    achei = usuarios.find(mq)
                    results = list(achei)
                    # se encontrar alguma coisa adicionar ao contador e exibir os valores
                    if results != []:
                        count_usuarios_jacadastrados += 1
                        print(f'{count_usuarios_jacadastrados} - Ja Cadastrado - {nome}')
                        # depois precisa fazer a verificação dos dados que ja estão no banco
                    else:

                        adicionar_usuario = {
                            "codigo" : codigo,
                            "nome" : nome,
                            "empresa" : empresa,
                            "login" : login,
                            "email" : email,
                            "idperfilacessosistema" : idperfilacessosistema,
                            "endereco_completo": consultar_endereco(endereco_completo_promotor),
                            "cep" : cep,
                            "logradouro" : logradouro,
                            "numero" : numero,
                            "complemento" : complemento,
                            "bairro" : bairro,
                            "cidade" : cidade,
                            "uf" : uf,
                            "latitude" : get_lat(endereco_completo_promotor),
                            "longitude" : get_lng(endereco_completo_promotor),
                            "telefone" : telefone,
                            "datanascimento" : datanascimento,
                            "rg" : rg,
                            "orgaoemissor" : orgaoemissor,
                            "cpf" : str(int(cpf)),
                            "banco" : banco,
                            "agencia" : agencia,
                            "conta" : conta,
                            "tipoconta" : tipoconta,
                            "ctpsnumero" : ctpsnumero,
                            "ctpsserie" : ctpsserie,
                            "ctpsestado" : ctpsestado,
                            "admissao" : admissao,
                            "desligamento" : desligamento,
                            "pis" : pis,
                            "custooperacional" : custooperacional,
                            "nacionalidade" : nacionalidade,
                            "estadocivil" : estadocivil,
                            "sexo" : sexo,
                            "status" : status,
                            "superior" : superior,
                            "data_inclusao" : str(datetime.timestamp(datetime.now())),
                            "data_alteracao" : ""
                        }


                        usuarios.insert_one(adicionar_usuario)
                        count_usuarios_cadastrados += 1
                        print(f'{count_usuarios_cadastrados}, {adicionar_usuario}')

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



print("")
print("Sistema encerrado")
print(f'Usuarios já cadastrados - {count_usuarios_jacadastrados}')
print(f'Usuarios novos cadastrados - {count_usuarios_cadastrados}')
print(f"Pdv's já cadastrados - {count_pdvs_jacadastrados}")
print(f"Pdv's novos cadastrados - {count_pdvs_jacadastrados}")