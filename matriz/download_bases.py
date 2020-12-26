import shutil
import requests
from win10toast import ToastNotifier
import pandas as pd
import os.path
from datetime import datetime, timedelta

print("Sistema Iniciado")
save_path = r'C:\root_pdv_temp'

def pasta():
    try:
        shutil.rmtree(save_path)
        print("pasta excluída")
        os.makedirs(save_path)
        print("pasta criada")
    except:
        os.makedirs(save_path)
        print("pasta criada")
pasta()

t = ToastNotifier()
now = datetime.now()
trintadias = datetime.now() + timedelta(29)

# ---------------------------------------------------------------------------------------- USUÁRIOS
file_usuarios = 'USUÁRIOS.xlsx'
path_usuarios = os.path.join(save_path, file_usuarios)

def baixar_usuarios():
    url_usuario = "http://api.grupogmpromo.pdvaction.com.br/api/usuariosistema/exportarxlsx"

    p_usuarios = {
            "Exportar": True,
            "Status": "",
            "Termo": "",
            "idUsuarioRequest": "5d42c679bc25f6225463fd93"
    }

    t.show_toast("Usuarios","Começou a baixar usuarios")
    res_usuarios = requests.post(url_usuario, json=p_usuarios)
    print("resposta web concluída")
    print("salvando arquivo na pasta")
    with open(path_usuarios, 'wb') as output:
        output.write(res_usuarios.content)
        print("base salva")

def ler_usuarios():
    wb_usuarios = pd.read_excel(path_usuarios, "Sheet1", usecols=any, engine='openpyxl')
    base_usuarios = pd.DataFrame(wb_usuarios).to_numpy()
    for usuario in base_usuarios:
        print(f'Usuários - {usuario[0]}')

# ---------------------------------------------------------------------------------------- ESTABELECIMENTOS
file_estabelecimentos = 'ESTABELECIMENTOS.xlsx'
path_estabelecimentos = os.path.join(save_path, file_estabelecimentos)

def baixar_estabelecimentos():
    url_lojas = "http://api.grupogmpromo.pdvaction.com.br/api/estabelecimento/exportarxlsx"

    p_estabelecimentos = {
        "Exportar": False,
        "OrderBy": "Codigo",
        "OrderType": "desc",
        "idUsuarioRequest": "5d42c679bc25f6225463fd93"}

    t.show_toast("Estabelecimentos","Começou a baixar estabelecimentos")
    res_estabelecimentos = requests.post(url_lojas, json=p_estabelecimentos)
    print("resposta web concluída")
    print("salvando arquivo na pasta")
    with open(path_estabelecimentos, 'wb') as output:
        output.write(res_estabelecimentos.content)
        print("base salva")

def ler_pdv():
    wb_pdvs = pd.read_excel(path_estabelecimentos, "Sheet1", usecols=any, engine='openpyxl')
    print("Leitura do arquivo estabelecimentos, concluída")
    base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()
    print("arquivo convertido em Data Frame")

    for loja in base_pdvs:
        print(f'Loja {loja[0]}')



# ---------------------------------------------------------------------------------------- MATRIZ
file_matriz = 'MATRIZ PDV COMPLETA.xlsx'
path_matriz = os.path.join(save_path, file_matriz)

def baixar_matriz():
    url_matriz = "http://api.grupogmpromo.pdvaction.com.br/api/relatorios/exportarxlsxmatriz"

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

    t.show_toast("Matriz","Começou a baixar a matriz")
    res_matriz = requests.post(url_matriz, json=p_matriz)
    print("resposta web concluída")
    print("salvando arquivo na pasta")
    with open(path_matriz, 'wb') as output:
        output.write(res_matriz.content)
        print("matriz salva")

def ler_matriz():
    wb_matriz = pd.read_excel(path_matriz, "Sheet1", usecols=any, engine='openpyxl')
    print("Leitura do arquivo matriz, concluída")
    base_matriz = pd.DataFrame(wb_matriz).to_numpy()
    print("arquivo convertido em Data Frame")

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

        print(f'Matriz - {i[0]}')



# ----------------------------------------------------------------------------------------
baixar_usuarios()
baixar_estabelecimentos()
baixar_matriz()

'''
Fazer o download das seguintes bases

- Estabelecimentos
- Usuários
- Matriz PDV
- Performance
- Registro de ponto
- Horas marca
- SKU's

Criar requests de cada arquivo.

Receber arquivos, e salvar em pasta temporária localmente, com o nome correto de cada arquivo.


PERFORMANCE


PRIMEIRO EXCLUIR RESGISTROA DO BANCO QUE CONTEM AS INFORMAÇÕES DO DIA ATUAL
SEGUNDO SUBIR AS INFORMAÇÕES DE PERFORMANCE POR MARCA DO DIA ATUAL.

'''