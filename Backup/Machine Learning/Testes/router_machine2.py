import pandas as pd
from Testes import mongo

# def processo():
#     distancia = calcular_distancia(coordenadas_usuario, coordenadas_pdv)
#
#     mongo.cadastrar_distancia(cpf_promotor, nome_promotor, endereco_completo_promotor, coordenadas_usuario,
#                               status_promotor,
#                               cod_pdv, nome_pdv, bandeira_pdv, endereco_completo_pdv, coordenadas_pdv, status_pdv,
#                               str(distancia)
#                               )
#     print(f'Usuario = {nome_promotor}, Pdv = {nome_pdv}, Distancia = {distancia}')

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
    # coordenadas_usuario = mongo.query_usuario(cpf_promotor)
    print(mongo.query_usuario(nome_promotor), nome_promotor)
    if mongo.query_usuario(nome_promotor):
        print(mongo.query_usuario(nome_promotor))




    # for i in base_pdvs:
    #     cod_pdv = str(i[0])
    #     nome_pdv = str(i[1])
    #     bandeira_pdv = str(i[2])
    #     logradouro_pdv = str(i[3])
    #     numero_pdv = str(i[4])
    #     bairro_pdv = str(i[5])
    #     cidade_pdv = str(i[6])
    #     uf_pdv = str(i[7])
    #     cep_pdv = str(i[8])
    #     status_pdv = str(i[11])
    #     endereco_completo_pdv = f'{logradouro_pdv},{numero_pdv},{bairro_pdv},{cidade_pdv},{uf_pdv},{cep_pdv}'
    #     coordenadas_pdv = mongo.query_estabelecimento(cod_pdv)
    #
    #     thread = Thread(target=processo)
    #
    #     thread.start()
