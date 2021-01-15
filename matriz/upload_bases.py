import pandas as pd
import os.path
from datetime import datetime, timedelta
import pymysql.cursors
import requests


print("Sistema Iniciado")
save_path = r'C:\root_pdv_temp'

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

now = datetime.now()
dia = now.day
mes = now.month
ano = now.year
hora = now.hour
mes = now.month
segundo = now.second

hj = now.strftime("%d-%m-%Y")

def dataconvertida(data):
    date1 = datetime.strptime(data, '%d/%m/%Y').strftime("%d/%m/%Y")
    print(date1)



# ---------------------------------------------------------------------------------------- DATABASE

db = pymysql.connect(
  host="35.199.123.132",
  user="root",
  password="12345",
  database="matriz",
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
  )
mycursor = db.cursor()

# sql1 = "DELETE FROM usuarios"
# sql2 = "DELETE FROM matriz_pdv"
# sql3 = "DELETE FROM ausencia"
# sql4 = "DELETE FROM estabelecimentos"
# sql5 = f"DELETE FROM planejados WHERE data = {hj}"
# sql6 = f"DELETE FROM executados WHERE data = {hj}"
#
#
# mycursor.execute(sql1)
# mycursor.execute(sql2)
# mycursor.execute(sql3)
# mycursor.execute(sql4)
# mycursor.execute(sql5)
# mycursor.execute(sql6)
#
#
# db.commit()
# ---------------------------------------------------------------------------------------- USUÁRIOS

file_usuarios = 'USUÁRIOS.xlsx'
path_usuarios = os.path.join(save_path, file_usuarios)
insertusuarios = []
def ler_usuarios():
  wb_usuarios = pd.read_excel(path_usuarios, "Sheet1", usecols=any, engine='openpyxl')
  base_usuarios = pd.DataFrame(wb_usuarios).to_numpy()

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

    if statusexclusao != "Inativo":
      val = (codigo,
             nome,
             empresa,
             login,
             email,
             idperfilacessosistema,
             cep,
             logradouro,
             numero,
             complemento,
             bairro,
             cidade,
             uf,
             latitude,
             longitude,
             telefone,
             datanascimento,
             rg,
             orgaoemissor,
             cpf,
             banco,
             agencia,
             conta,
             tipoconta,
             ctpsnumero,
             ctpsserie,
             ctpsestado,
             admissao,
             desligamento,
             pis,
             custooperacional,
             nacionalidade,
             estadocivil,
             sexo,
             status,
             superior,
             datainclusao,
             dataalteracao)
      insertusuarios.append(val)


  sqlusuarios = "INSERT INTO usuarios (codigo, " \
            "nome, " \
            "empresa, " \
            "login, " \
            "email, " \
            "idperfilacessosistema, " \
            "cep, " \
            "logradouro, " \
            "numero, " \
            "complemento, " \
            "bairro, " \
            "cidade, " \
            "uf, " \
            "latitude, " \
            "longitude, " \
            "telefone, " \
            "datanascimento, " \
            "rg, " \
            "orgaoemissor, " \
            "cpf, " \
            "banco, " \
            "agencia, " \
            "conta, " \
            "tipoconta, " \
            "ctpsnumero, " \
            "ctpsserie, " \
            "ctpsestado, " \
            "admissao, " \
            "desligamento, " \
            "pis, " \
            "custooperacional, " \
            "nacionalidade, " \
            "estadocivil, " \
            "sexo, " \
            "status, " \
            "superior, " \
            "datainclusao, " \
            "dataalteracao) " \
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  mycursor.executemany(sqlusuarios, insertusuarios)
  db.commit()
  print("Usuários concluído")

# ---------------------------------------------------------------------------------------- ESTABELECIMENTOS

file_estabelecimentos = 'ESTABELECIMENTOS.xlsx'
path_estabelecimentos = os.path.join(save_path, file_estabelecimentos)
insertestabelecimentos = []
def ler_estabelecimentos():
  wb_pdvs = pd.read_excel(path_estabelecimentos, "Sheet1", usecols=any, engine='openpyxl')
  base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()
  insert = []
  for i in base_pdvs:
    datainclusaoregistro = i[0]
    codigorede = i[1]
    rede = i[2]
    codigobandeira = i[3]
    bandeira = str(i[4])
    codigo = str(i[5])
    nome = str(i[6])
    cnpj = str(i[7])
    cep = str(i[8]).replace("-", "")
    logradouro = str(i[9])
    numero = str(i[10])
    complemento = str(i[11])
    bairro = str(i[12])
    cidade = str(i[13])
    uf = str(i[14])
    latitude = str(i[15])
    longitude = str(i[16])
    regional = str(i[17])
    zona = i[18]
    status = str(i[19])
    endereco_completo = str(f'{logradouro},' \
                            f' {numero}, ' \
                            f'{bairro}, ' \
                            f'{cidade}, ' \
                            f'{uf}, ' \
                            f'cep {cep}')




    val = (codigo,
           bandeira,
           nome,
           logradouro,
           numero,
           bairro,
           cidade,
           uf,
           cep,
           endereco_completo,
           cnpj,
           latitude,
           longitude,
           regiao(uf),
           str(zona),
           status)
    insertestabelecimentos.append(val)


  sqlestabelecimentos = "INSERT INTO estabelecimentos (cod_loja, " \
          "bandeira, " \
          "nome, " \
          "logradouro, " \
          "numero_logradouro, " \
          "bairro, " \
          "cidade, " \
          "uf, " \
          "cep, " \
          "endereco_completo, " \
          "cnpj, " \
          "latitude, " \
          "longitude, " \
          "regional, " \
          "zona, " \
          "status) " \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  mycursor.executemany(sqlestabelecimentos, insertestabelecimentos)
  db.commit()
  print("Estabelecimentos concluído")


# ---------------------------------------------------------------------------------------- AUSENCIA

file_ausencia = 'AUSENCIA.xlsx'
path_ausencia = os.path.join(save_path, file_ausencia)
insertausencia = []

def ler_ausencia():
  wb_aus = pd.read_excel(path_ausencia, "Sheet1", usecols=any, engine='openpyxl')
  base_ausencia = pd.DataFrame(wb_aus).to_numpy()
  insertausencia = []
  for i in base_ausencia:
        data = str(i[0])
        statususuario = str(i[1])
        nome = str(i[2])
        tipo = str(i[3])
        lider = str(i[4])
        situacao = str(i[5])

        val = (data, statususuario, nome, tipo, str(lider), situacao)
        insertausencia.append(val)

  sqlausencia = "INSERT INTO ausencia (data,statususuario,nome,tipo,lider,situacao) VALUES (%s,%s,%s,%s,%s,%s)"
  mycursor.executemany(sqlausencia, insertausencia)
  db.commit()
  print("Ausencia concluído")

# ---------------------------------------------------------------------------------------- PLANEJADOS

file_planejados = 'PLANEJADOS.xlsx'
path_planejados = os.path.join(save_path, file_planejados)
insertplanejados = []

def ler_planejados():
  wb_plan = pd.read_excel(path_planejados, "Sheet1", usecols=any, engine='openpyxl')
  base_planejados = pd.DataFrame(wb_plan).to_numpy()
  insertplanejados = []

  def verificar_for(base, visita):
      for i in base:
          if i[0] == visita:
              return True
          else:
              False

  for i in base_planejados:
      data = str(i[0])
      statusatual = str(i[1])
      nomesuperior = str(i[2])
      nomeusuario = str(i[3])
      bandeira = str(i[4])
      estabelecimento = str(i[5])
      est = estabelecimento.split(" - ")
      codloja = est[0]
      uf = str(i[6])
      cliente = str(i[7])
      fotosantes = str(i[8])
      fotosdepois = str(i[9])
      esperadas = str(i[10])
      codvisita = f"{cliente} - {codloja}"

      val = (codvisita, cliente, codloja, estabelecimento, bandeira, uf, nomeusuario, statusatual, nomesuperior, data)

      if cliente.find("/") == -1:
          if verificar_for(insertplanejados, codvisita) == True:
              a=""
          else:
            insertplanejados.append(val)
      else:
          a=""




  sqlplanejados = "INSERT INTO planejados (codvisita, cliente, codloja, estabelecimento, bandeira, uf, nomeusuario, statusatual, nomesuperior, data) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  mycursor.executemany(sqlplanejados, insertplanejados)
  db.commit()


  print("Planejados concluído")

# ---------------------------------------------------------------------------------------- EXECUTADOS

file_executados = 'EXECUTADOS.xlsx'
path_executados = os.path.join(save_path, file_executados)
insertexecutados = []

def ler_executados():
  wb_exec = pd.read_excel(path_executados, "Sheet1", usecols=any, engine='openpyxl')
  base_executados = pd.DataFrame(wb_exec).to_numpy()
  insertexecutados = []
  for i in base_executados:
      usuariosistema = str(i[0])
      nomesuperior = str(i[1])
      marca = str(i[2])
      estabelecimento = str(i[3])
      est = estabelecimento.split(" - ")
      codloja = est[0]
      foiabastecido = str(i[4])
      duracao = str(i[5])
      horainicio = str(i[6])
      horafinal = str(i[7])
      data = str(i[8]).replace("-", "/")
      codvisita = f"{marca} - {codloja}"

      val = (codvisita, usuariosistema, nomesuperior, marca, codloja, estabelecimento, foiabastecido, duracao, horainicio, horafinal, data)
      insertplanejados.append(val)

  sqlexecutados = "INSERT INTO executados (codvisita, usuariosistema, nomesuperior, marca, codloja, estabelecimento, foiabastecido, duracao, horainicio, horafinal, data) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  mycursor.executemany(sqlexecutados, insertexecutados)
  db.commit()

  print(insertexecutados)
  print("Executados concluído concluído")

# ---------------------------------------------------------------------------------------- MATRIZ - ok

file_matriz = 'MATRIZ PDV COMPLETA.xlsx'
path_matriz = os.path.join(save_path, file_matriz)
insertmatriz = []
def ler_matriz():
  wb_matriz = pd.read_excel(path_matriz, "Sheet1", usecols=any, engine='openpyxl').fillna("0")
  base_matriz = pd.DataFrame(wb_matriz).to_numpy()




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
    logradouro = str(i[10])
    bairro = str(i[11])
    cep = str(i[12]).replace("-", "")
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

    val = (str(codvisita),
           str(cliente),
           str(familia),
           str(codloja),
           str(loja),
           str(bandeira),
           str(logradouro),
           str(bairro),
           str(cep),
           str(latitude),
           str(longitude),
           str(cnpj),
           str(regional),
           str(zona),
           str(uf),
           str(gestorcoordenador),
           str(supervisor),
           str(lider),
           str(cargocampo),
           str(promotor),
           str(tipoagendamento),
           str(diasporsemana),
           str(seg), str(ter), str(qua), str(qui), str(sex), str(sab), str(dom),
           str(tarefa),
           str(trademarketing),
           str(departamento),
           str(inicio),
           str(termino),
           str(nomeusuarioinclusao),
           str(dataultimaalteracao),
           str(usuarioultimaalteracao))
    insertmatriz.append(val)

  sqlmatriz = "INSERT INTO matriz_pdv (" \
              "cod_visita, " \
              "cliente, " \
              "familia, " \
              "codloja, " \
              "loja, " \
              "bandeira, " \
              "logradouro, " \
              "bairro, " \
              "cep, " \
              "latitude, " \
              "longitude, " \
              "cnpj, " \
              "regional, " \
              "zona, " \
              "uf, " \
              "terceira_hierarquia, " \
              "segunda_hierarquia, " \
              "primeira_hierarquia, " \
              "perfil, " \
              "promotor, " \
              "tipoagendamento, " \
              "diasporsemana, " \
              "seg, ter, qua, qui, sex, sab, dom, " \
              "tarefa, " \
              "trademarketing, " \
              "departamento, " \
              "inicio, " \
              "termino, " \
              "nomeusuarioinclusao, " \
              "dataultimaalteracao, " \
              "usuarioultimaalteracao) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  mycursor.executemany(sqlmatriz, insertmatriz)
  db.commit()
  print("Matriz concluído")


# ---------------------------------------------------------------------------------------- FUNÇÔES

ler_usuarios()

ler_estabelecimentos()

ler_ausencia()

ler_matriz()

ler_planejados()

ler_executados()



'''
Fazer a leitura das seguintes bases

- Estabelecimentos
- Usuários
- Matriz PDV
- Performance
- Registro de ponto
- Horas marca
- SKU's

Ler arquivos da pasta temporária e em seguida fazer o upload para baco de dados mysql
'''