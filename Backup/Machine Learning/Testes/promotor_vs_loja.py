import pandas as pd
import requests
import pymongo
from threading import Thread

# API GOOGLE
api_key = 'AIzaSyAaJ4vzbbd9w7rhrYaCm7IoYhuhr8um2Eg'

def processo():
    distancia = calcular_distancia(endereco_completo_promotor, endereco_completo_pdv)
    cadastrar_no_banco(
        cpf=cpf_promotor,
        nome_usuario=nome_promotor,
        endereco_completo_usuario=endereco_completo_promotor,
        latitude_usuario=get_lat(endereco_completo_promotor),
        longitute_usuario=get_lng(endereco_completo_promotor),
        status_usuario=status_promotor,
        cod_pdv=cod_pdv,
        nome_pdv=nome_pdv,
        bandeira=bandeira_pdv,
        endereco_completo_pdv=endereco_completo_pdv,
        latitude_pdv=get_lat(endereco_completo_pdv),
        longitude_pdv=get_lng(endereco_completo_pdv),
        status_pdv=status_pdv,
        distancia=distancia
    )


def cadastrar_no_banco(cpf, nome_usuario, endereco_completo_usuario, latitude_usuario, longitute_usuario,
                       status_usuario, cod_pdv, nome_pdv, bandeira, endereco_completo_pdv, latitude_pdv, longitude_pdv, status_pdv,  distancia):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client["Infinity_Way"]
    usuario_vs_estabelecimentos = db["usuario_vs_estabelecimentos"]

    adicionar = {
        "origem": [{
            "cpf": cpf,
            "nome_usuario": nome_usuario,
            "endereco_completo_usuario": endereco_completo_usuario,
            "latitude_usuario": latitude_usuario,
            "longitute_usuario": longitute_usuario,
            "status_usuario": status_usuario

        }],
        "destino": [{
            "cod_pdv": cod_pdv,
            "nome_pdv": nome_pdv,
            "bandeira": bandeira,
            "endereco_completo_pdv": endereco_completo_pdv,
            "latitude_pdv": latitude_pdv,
            "longitude_pdv": longitude_pdv,
            "status_pdv":status_pdv
        }],
        "percurso":  distancia

    }

    # }
    usuario_vs_estabelecimentos.insert_one(adicionar)
    return print(f'{distancia} / {nome_usuario} / {nome_pdv}')

def calcular_distancia(origem, destino):
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' \
          f'{origem}&destinations={destino}&mode=bicycling&language=pt-BR&key={api_key}'
    r = requests.get(url).json()
    rows = r["rows"]
    di = []
    du = []
    # elements = rows["elements"]
    # distance = elements["distance"]
    # distancia = distance["value"]
    for a in rows:
        elements = a["elements"]
        for b in elements:
            if b["status"] != "OK":
                di.append(0)
                du.append(0)
            else:
                distance = b["distance"]
                duration = b["duration"]
                for c in distance.values():
                    di.append(c)
                for d in duration.values():
                    du.append(d)

    try:
        distancia = int(di[1])/1000
        tempo_percorrido = (int(du[1])/60)/60
        return {"distancia":distancia, "tempo":tempo_percorrido}

    except:
        distancia = 0.0
        tempo_percorrido = 0.0
        return distancia

def get_lat(endereco):
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

# leitura e listagem da base de usuários
wb_promotor = pd.read_excel("base.xlsx", "usuarios", usecols=any)
base_promotores = pd.DataFrame(wb_promotor).to_numpy()
wb_pdvs = pd.read_excel("base.xlsx", "pdvs", usecols=any)
base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()

for i in base_promotores:
    cpf_promotor = str(i[0])
    nome_promotor = str(i[1])
    perfil_promotor = str(i[2])
    sexo_promotor = str(i[3])
    contato_promotor = str(i[4])
    status_promotor = str(i[5])
    logradouro_promotor = str(i[6])
    numero_promotor = str(i[7])
    bairro_promotor = str(i[8])
    cidade_promotor = str(i[9])
    uf_promotor = str(i[10])
    cep_promotor = str(i[11])
    inicio_jornada_promotor = str(i[14])
    fim_jornada_promotor = str(i[15])
    pausa_jornada_promotor = str(i[16])
    meio_transporte_promotor = str(i[17])
    jornada_semana_promotor = str(i[18])
    descanso_semanal_promotor = str(i[19])
    cpf_supervisor = str(i[20])
    nome_supervisor = str(i[21])
    endereco_completo_promotor = f'{logradouro_promotor},' \
                        f' {numero_promotor}, ' \
                        f'{bairro_promotor}, ' \
                        f'{cidade_promotor}, ' \
                        f'{uf_promotor}, ' \
                        f'cep {cep_promotor}'



    for i in base_pdvs:
        cod_pdv = str(i[0])
        nome_pdv = str(i[1])
        bandeira_pdv = str(i[2])
        logradouro_pdv = str(i[3])
        numero_pdv = str(i[4])
        bairro_pdv = str(i[5])
        cidade_pdv = str(i[6])
        uf_pdv = str(i[7])
        cep_pdv = str(i[8])
        status_pdv = str(i[11])
        endereco_completo_pdv = f'{logradouro_pdv},{numero_pdv},{bairro_pdv},{cidade_pdv},{uf_pdv},{cep_pdv}'

        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client["Infinity_Way"]
        usuario_vs_estabelecimentos = db["usuario_vs_estabelecimentos"]
        myquery = {"origem.cpf": cpf_promotor, "destino.cod_loja": cod_pdv}
        mydoc = usuario_vs_estabelecimentos.find(myquery)
        comparacao = []
        for x in mydoc:
            origem = x["origem"]
            destino = x["destino"]
            for i in origem:
                cpf = i["cpf"]
            for i in destino:
                cod_loja = i["cod_loja"]
                found = {"origem.cpf": cpf, "destino.cod_loja": cod_loja}
                comparacao.append(found)


        if myquery != comparacao:
            thread = Thread(target=processo)

            thread.start()


        else:
            print(nome_promotor, nome_pdv)

