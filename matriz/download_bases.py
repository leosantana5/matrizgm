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
    with open(path_usuarios, 'wb') as output:
        output.write(res_usuarios.content)
        print(f"base {file_usuarios} - salvo com sucesso")

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
    with open(path_estabelecimentos, 'wb') as output:
        output.write(res_estabelecimentos.content)
        print(f"base {file_estabelecimentos} - salvo com sucesso")

def ler_pdv():
    wb_pdvs = pd.read_excel(path_estabelecimentos, "Sheet1", usecols=any, engine='openpyxl')
    print("Leitura do arquivo estabelecimentos, concluída")
    base_pdvs = pd.DataFrame(wb_pdvs).to_numpy()
    print("arquivo convertido em Data Frame")

    for loja in base_pdvs:
        print(f'Loja {loja[0]}')


# ---------------------------------------------------------------------------------------- AUSENCIA
file_ausencia = 'AUSENCIA.xlsx'
path_ausencia = os.path.join(save_path, file_ausencia)
def baixar_ausencia():
    url_ausencia = "http://api.grupogmpromo.pdvaction.com.br/api/relatorios/exportarxlsxratrasados"

    p_ausencia = {
        "DataRequest": now.strftime("%Y-%m-%dT03:00:00.000Z"),
        "IdUsuarioRequest": "5d42c679bc25f6225463fd93",
    }

    t.show_toast("Ausencia", "Começou a baixar a Ausencia")
    res_ausencia = requests.post(url_ausencia, json=p_ausencia)
    with open(path_ausencia, 'wb') as output:
        output.write(res_ausencia.content)
        print(f"Base {file_ausencia} - Salvo com sucesso")

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
    with open(path_matriz, 'wb') as output:
        output.write(res_matriz.content)
        print(f"Base {file_matriz} - Salvo com sucesso")

# ---------------------------------------------------------------------------------------- ROTEIROS PLANEJADOS

file_planejados = 'PLANEJADOS.xlsx'
path_planejados = os.path.join(save_path, file_planejados)

def baixar_planejados():
    url_planejados = "http://api.grupogmpromo.pdvaction.com.br/api/relatorios/exportarxlsxravaliacaofotos"

    p_planejados = {
        "DataFinal": now.strftime("%Y-%m-%dT03:00:00.000Z"),
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

    t.show_toast("Roteiros Planejados","Começou a baixar os roteiros planejados")
    res_planejados = requests.post(url_planejados, json=p_planejados)
    with open(path_planejados, 'wb') as output:
        output.write(res_planejados.content)
        print(f"Base {file_planejados} - Salvo com sucesso")

# ---------------------------------------------------------------------------------------- ROTEIROS PLANEJADOS

file_executados = 'EXECUTADOS.xlsx'
path_executados = os.path.join(save_path, file_executados)

def baixar_executados():
    url_executados = "http://api.grupogmpromo.pdvaction.com.br/api/horapormarca/exportarxlsx"

    p_executados = {
        "DataFinal": now.strftime("%Y-%m-%dT03:00:00.000Z"),
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

    t.show_toast("Roteiros Executados","Começou a baixar os roteiros executados")
    res_executados = requests.post(url_executados, json=p_executados)
    with open(path_executados, 'wb') as output:
        output.write(res_executados.content)
        print(f"Base {file_executados} - Salvo com sucesso")


# ----------------------------------------------------------------------------------------
baixar_usuarios()
baixar_estabelecimentos()
baixar_ausencia()
baixar_matriz()
baixar_planejados()
baixar_executados()


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