import pandas as pd
import requests
from geopy import distance as gp
import pymongo


# API GOOGLE
api_key = 'AIzaSyAaJ4vzbbd9w7rhrYaCm7IoYhuhr8um2Eg'

destination_addresses = "Rua Professor Eldemar Alves de Oliveira, 176"
origin_addresses = "Rua Eduardo Chaves, 183"

cds_1 = (-23.421531, -46.527697)
cds_2 = (-23.523583, -46.628641)

def cadastrar_no_banco(cpf,nome_usuario,endereco_completo_usuario,latitude_usuario,longitute_usuario, status_usuario,
                       cod_pdv, nome_pdv, bandeira, endereco_completo_pdv, latitude_pdv, longitude_pdv,status_pdv,
                       distancia):
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
    return print(adicionar)

def blabla(origem, destino):
    distancia = gp.distance(origem,destino).kilometers
    return distancia

# print(blabla(cds_2,cds_1))



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




def calc_dist_1loja_vs_todos_promotores(loja, promotores):
    url = (
        f'https://maps.googleapis.com/maps/api/distancematrix/json?origins='
        f'{loja}&destinations={promotores}&mode=bicycling&language=pt-BR&key={api_key}')
    r = requests.get(url).json()
    return print(r)


# BASE DE PROMOTORES ---------------------

wb_promotor = pd.read_excel("matriz.xlsx", "BASE_PROMOTOR", usecols=any)
base_promotores = pd.DataFrame(wb_promotor).to_numpy()

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
    lat_promotor = str(i[12])
    lng_promotor = str(i[13])
    inicio_jornada_promotor = str(i[14])
    fim_jornada_promotor = str(i[15])
    pausa_jornada_promotor = str(i[16])
    meio_transporte_promotor = str(i[17])
    jornada_semana_promotor = str(i[18])
    descanso_semanal_promotor = str(i[19])
    cpf_supervisor = str(i[20])
    nome_supervisor = str(i[21])
    endereco_completo = f'{logradouro_promotor},' \
                        f' {numero_promotor}, ' \
                        f'{bairro_promotor}, ' \
                        f'{cidade_promotor}, ' \
                        f'{uf_promotor}, ' \
                        f'cep {cep_promotor}'
    cords_promotor = f'{lat_promotor}, {lng_promotor}'
    # print(blabla(cords_promotor, cds_2))
    distancia_calculada = calcular_distancia(endereco_completo, origin_addresses)
    cadastrar_no_banco(cpf_promotor,nome_promotor,endereco_completo,lat_promotor,longitute_usuario=0,status_usuario=status_promotor,cod_pdv=123,nome_pdv="nome da loja",bandeira="Bandeira de teste", endereco_completo_pdv="Eduardo Chaves, 183", latitude_pdv=-23.523583, longitude_pdv=-46.628641, status_pdv=1, distancia=distancia_calculada )


# BASE DE VISITAS ------------------------

wb_visitas = pd.read_excel("matriz.xlsx", "BASE_DE_VISITAS", usecols=any)
base_visitas = pd.DataFrame(wb_visitas).to_numpy()

for i in base_visitas:
    cod_visita = i[0]
    cliente = i[1]
    freq = i[2]
    hora = i[3]
    cod_pdv = i[4]
    bandeira_pdv = i[5]
    nome_pdv = i[6]
    logradouro_pdv = i[7]
    numero_pdv = i[8]
    bairro_pdv = i[9]
    uf_pdv = i[10]
    cep_pdv = i[11]
    lat_pdv = i[12]
    lng_pdv = i[13]
    hora_abertura_pdv = i[14]
    visita_fixa_dia_sim_dia_nao = i[15]
    permitir_visitas_dia_seguido = i[16]
    visitas_fixas_todos_os_dias = i[17]
    visita_fixa_as_segundas = i[18]
    visita_fixa_as_tercas = i[19]
    visita_fixa_as_quartas = i[20]
    visita_fixa_as_quintas = i[21]
    visita_fixa_as_sextas = i[22]
    visita_fixa_aos_sabados = i[23]
    visita_fixa_aos_domingos = i[24]
    primeira_visita_do_dia_ = _exigencia = i[25]
