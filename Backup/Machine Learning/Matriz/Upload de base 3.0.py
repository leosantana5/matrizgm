from win10toast import ToastNotifier
import requests
import pandas as pd
import os.path
from datetime import datetime, timedelta
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

# ----------------------------------------------------------------------------------------

trintadias = datetime.now() + timedelta(29)

diat = trintadias.day
mest = trintadias.month
anot = trintadias.year
now = datetime.now()
hora = now.hour
minuto = now.minute

testedata = trintadias.strftime("%Y-%m-%dT03:00:00.000Z")
dia = now.day
mes = now.month
ano = now.year
hora = now.hour
mes = now.month
segundo = now.second

trintaamericano = f'{anot}-0{mest}-{diat}T03:00:00.000Z'
diaamericano = f'{ano}-{mes}-{dia}T03:00:00.000Z'


save_path = 'M:/2 - PDV Action/'
save_path2= 'M:/2 - PDV Action/Performance/'

print("Sistema Iniciado")
# ----------------------------------------------------------------------------------------

url_usuario = "http://api.grupogmpromo.pdvaction.com.br/api/usuariosistema/exportarxlsx"
file_usuarios = 'Usuários PDV.xlsx'
path_usuarios = os.path.join(save_path, file_usuarios)

url_lojas = "http://api.grupogmpromo.pdvaction.com.br/api/estabelecimento/exportarxlsx"
file_estabelecimentos = 'Estabelecimentos PDV.xlsx'
path_estabelecimentos = os.path.join(save_path, file_estabelecimentos)

url_matriz = "http://api.grupogmpromo.pdvaction.com.br/api/relatorios/exportarxlsxmatriz"
file_matriz = 'MATRIZ PDV COMPLETA.xlsx'
path_matriz = os.path.join(save_path, file_matriz)

url_performance = "http://api.grupogmpromo.pdvaction.com.br/api/relatorios/exportarxlsxrelatorioperformance"
file_performance = f'Performance - {dia}-{mes}-{ano}.xlsx'
path_performance = os.path.join(save_path2, file_performance)

url_performance_cliente = "http://api.grupogmpromo.pdvaction.com.br/api/relatorios/exportarxlsxrperformancemarca"
file_performance_cliente = f'Performance cliente - {dia}-{mes}-{ano}.xlsx'
path_performance_cliente = os.path.join(save_path2, file_performance_cliente)

url_registrodeponto = "http://api.grupogmpromo.pdvaction.com.br/api/registrodeponto/exportarxlsxlinha"
t = ToastNotifier()

# ----------------------------------------------------------------------------------------

p_matriz = {
    "DataFinal": trintadias.strftime("%Y-%m-%dT03:00:00.000Z"),
    "DataInicial": now.strftime("%Y-%m-%dT03:00:00.000Z"),
    "IdBandeira": "",
    "IdUsuarioRequest": "5d42c679bc25f6225463fd93",
    "IdsEstabelecimentos": "",
    "IdsFamiliasProdutos": "",
    "IdsSupervisoresSistema": "",
    "IdsUsuariosSistema": "",
    "Paginacao": {
        "OrderBy": "",
        "OrderType": "desc",
        "Skip": 0,
        "Top": 0}
}

p_performance = {
    "DataFinal": now.strftime("%Y-%m-%dT03:00:00.000Z"),
    "DataInicial": now.strftime("%Y-%m-%dT03:00:00.000Z"),
    "Estados":"",
    "IdBandeira": "",
    "IdUsuarioRequest": "5d42c679bc25f6225463fd93",
    "IdsEstabelecimentos": "",
    "IdsFamiliasProdutos": "",
    "IdsSupervisoresSistema": "",
    "IdsUsuariosSistema": "",
    "Paginacao": {
        "OrderBy": "Data",
        "OrderType": "desc",
        "Skip": 0,
        "Top": 10}
}

p_performance_cliente = {
    "DataFinal": "2020-12-16T02:59:59.999Z",
    "DataInicial": "2020-12-19T02:59:59.999Z",
    "Estados":"",
    "IdBandeira": "",
    "IdUsuarioRequest": "5d42c679bc25f6225463fd93",
    "IdsEstabelecimentos": "",
    "IdsFamiliasProdutos": "",
    "IdsSupervisoresSistema": "",
    "IdsUsuariosSistema": "",
    "Paginacao": {
        "OrderBy": "Data",
        "OrderType": "desc",
        "Skip": 0,
        "Top": 10}
}

p_estabelecimentos = {
    "Exportar": False,
    "OrderBy": "Codigo",
    "OrderType": "desc",
    "idUsuarioRequest": "5d42c679bc25f6225463fd93"}

p_usuarios = {
        "Exportar": True,
        "Status": "",
        "Termo": "",
        "idUsuarioRequest": "5d42c679bc25f6225463fd93"
}

p_resgistrodeponto = {
    "DataFinal": "2020-12-21T02:59:59.999Z",
    "DataInicial": "2020-11-21T03:00:00.000Z",
    "ExibirApenasAbonado": False,
    "IdUsuarioRequest": "5d42c679bc25f6225463fd93",
    "IdsMarcas": [],
    "IdsSupervisoresSistema": "",
    "IdsUsuariosSistema": "",
    "Paginacao": {
        "OrderBy": "StatusUsuario",
        "OrderType": "desc",
        "Skip": 0,
        "Top": 100},
    "StatusUsuario":[
        "Ativo",
        "Ferias",
        "Licenca",
        "AvisoPrevio",
        "Suspenso",
        "Inativo"
    ],
    "Perfis": [
        # "promotor",
        # "promotor548",
        # "parttime4",
        # "parttime5",
        # "parttime6",
        # "express",
        # "intermitente",
        # "terceirizado",
        # "aguia",
        # "supervisor",
        # "liderSupervisor",
        # "coordenador",
        # "trade",
        # "tradeSuporte",
        # "tradeCoordenador",
        # "gerente",
        # "rh",
        # "promotorpromotor8sabado",
        # "promotorlivre",
    ]
}

# ___________________________________________________________________________________

def baixar_matriz():
    t.show_toast("Matriz","Começou a baixar a matriz, o léo é lindo")
    res_matriz = requests.post(url_matriz, json=p_matriz)
    print("resposta web concluída")
    print("salvando arquivo na pasta")
    with open(path_matriz, 'wb') as output:
        output.write(res_matriz.content)
        print("matriz salva")

def baixar_performance():
    t.show_toast("Performance","Começou a baixar a performance")

    res_performance = requests.post(url_performance, json=p_performance)
    with open(path_performance, 'wb') as output:
        output.write(res_performance.content)

def baixar_performance_cliente():
    t.show_toast("Performance", "Começou a baixar a performance por cliente")

    res_performance_cliente = requests.post(url_performance_cliente, json=p_performance_cliente)
    with open(path_performance_cliente, 'wb') as output:
        output.write(res_performance_cliente.content)

def baixar_estabelecimentos():
    t.show_toast("Estabelecimentos","Começou a baixar estabelecimentos")
    res_estabelecimentos = requests.post(url_lojas, json=p_estabelecimentos)
    with open(path_estabelecimentos, 'wb') as output:
        output.write(res_estabelecimentos.content)

def baixar_usuarios():
    t.show_toast("Usuarios","Começou a baixar usuarios")
    res_usuarios = requests.post(url_usuario, json=p_usuarios)
    with open(path_usuarios, 'wb') as output:
        output.write(res_usuarios.content)

def baixar_registrodeponto():
    t.show_toast("Registro de ponto","Começou a baixar registro de ponto")
    file_registroponto = 'Registro de Ponto.xlsx'
    completeName_registroponto = os.path.join(save_path, file_registroponto)
    res_registroponto = requests.post(url_usuario, json=p_resgistrodeponto)
    with open(completeName_registroponto, 'wb') as output:
        output.write(res_registroponto.content)

# ___________________________________________________________________________________
print("")
# baixar_estabelecimentos()
# print("Base de estabelecimentos baixada")
# baixar_performance()
# print("Base de performance baixada")
# baixar_performance_cliente()
# print("Base de performance baixada")
# baixar_usuarios()
# print("Base de usuários baixada")
baixar_matriz()


# LEITURA DAS BASES  ------------------------------

def ler_pdv():
    wb_pdvs = pd.read_excel(path_estabelecimentos, "Sheet1", usecols=any)
    base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()
    for loja in base_pdvs:
        print(loja)

print("")
# ______________
def ler_usuarios():
    wb_usuarios = pd.read_excel(path_usuarios, "Sheet1", usecols=any)
    base_usuarios = pd.DataFrame(wb_usuarios).to_numpy()
    for usuario in base_usuarios:
        print("")
# ______________
def ler_perf_cliente():
    wb_performance_cliente = pd.read_excel(path_performance_cliente, "Sheet1", usecols=any)
    base_performance_cliente = pd.DataFrame(wb_performance_cliente).to_numpy()
    for linha in base_performance_cliente:
        print("")
# ______________

print("")
def ler_matriz():
    wb_matriz = pd.read_excel(path_matriz, "Sheet1", usecols=any)
    print("Leitura do arquivo matriz, concluída")
    base_matriz = pd.DataFrame(wb_matriz).to_numpy()
    print("arquivo convertido em Data Frame")
    insert1 = []
    count_matriz = 0
    for i in base_matriz:
        trademarketing = str(i[0])
        departamento = str(i[1])
        inicio = str(i[2])
        termino = str(i[3])
        codigomarcaloja = str(i[4])
        codigorede = str(i[5])
        bandeira = str(i[6])
        codloja = str(i[7])
        loja = str(i[8])
        cnpj = str(i[9])
        textoendereco = str(i[10])
        bairro = str(i[11])
        cep = str(i[12])
        latitude = str(i[13])
        longitude = str(i[14])
        codcliente = str(i[15])
        comercial = str(i[16])
        regional = str(i[17])
        zona = str(i[18])
        uf = str(i[19])
        gestorcoordenador = str(i[20])
        supervisor = str(i[21])
        lider = str(i[22])
        cargocampo = str(i[23])
        status = str(i[24])
        promotor = str(i[25])
        familia = str(i[26])
        cliente = str(i[27])
        tipoagendamento = str(i[28])
        diasporsemana = str(i[29])
        seg = str(i[30])
        ter = str(i[31])
        qua = str(i[32])
        qui = str(i[33])
        sex = str(i[34])
        sab = str(i[35])
        dom = str(i[36])
        tarefa = str(i[37])
        nomeusuarioinclusao = str(i[38])
        frequencia = str(i[39])
        viabilidade = str(i[40])
        valorvisitaprovisionado = str(i[41])
        valornegociado = str(i[42])
        valorloja = str(i[43])
        avisoprevio = str(i[44])
        comissao = str(i[45])
        datainiciooperacao = str(i[46])
        horasistema = str(i[47])
        qtdsku = str(i[48])
        dataultimaalteracao = str(i[49])
        usuarioultimaalteracao = str(i[50])
        codvisita = f"{cliente} - {codloja}"

        val = (codvisita, trademarketing, departamento, inicio, termino, codigomarcaloja, codigorede, bandeira, codloja, loja, cnpj, textoendereco, bairro, cep, latitude, longitude, codcliente, comercial, regional, zona, uf, gestorcoordenador, supervisor, lider, cargocampo, status, promotor, familia, cliente, tipoagendamento, diasporsemana, seg, ter, qua, qui, sex, sab, dom, tarefa, nomeusuarioinclusao, frequencia, viabilidade, valorvisitaprovisionado, valornegociado, valorloja, avisoprevio, comissao, datainiciooperacao, horasistema, qtdsku, dataultimaalteracao, usuarioultimaalteracao)
        sql = "INSERT INTO matriz_pdv (cod_visita, TradeMarketing, Departamento, Inicio, Termino, CodigoMarcaLoja, CodigoRede, Bandeira, CodLoja, Loja, CNPJ, TextoEndereco, Bairro, CEP, Latitude, Longitude, CodCliente, Comercial, Regional, Zona, UF, GestorCoordenador, Supervisor, Lider, CargoCampo, Status, Promotor, Familia, Cliente, TipoAgendamento, DiasPorSemana, Seg, Ter, Qua, Qui, Sex, Sab, Dom, Tarefa, NomeUsuarioInclusao, Frequencia, Viabilidade, ValorVisitaProvisionado, ValorNegociado, ValorLoja, AvisoPrevio, Comissao, DataInicioOperacao, HoraSistema, QtdSku, DataUltimaAlteracao, UsuarioUltimaAlteracao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        insert1.append(val)

        count_matriz += 1

        print(count_matriz)
    print(insert1)
    mycursor = db.cursor()
    mycursor.executemany(sql, insert1)
    db.commit()
    print(mycursor.rowcount, "was inserted.")


# ______________
def ler_perf():
    wb_performance = pd.read_excel(path_performance, "Sheet1", usecols=any)
    base_performance = pd.DataFrame(wb_performance).to_numpy()
    for linha in base_performance:
        print("")

thread = Thread(target = ler_matriz())
thread.start()


print("FIM")
