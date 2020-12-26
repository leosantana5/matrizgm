from selenium import webdriver
import os
import shutil
import time


# ---------------------------------------------------------------------------------
try:
    shutil.rmtree(r'C:\testes')
    print("pasta não existe")
except:

    os.makedirs(r'C:\testes')
    print("pasta criada")

# ---------------------------------------------------------------------------------

options = webdriver.ChromeOptions()
prefs = {
"download.default_directory": r"C:\testes",
"download.prompt_for_download": False,
"download.directory_upgrade": True
}
options.add_experimental_option('prefs', prefs)
chrome = webdriver.Chrome(executable_path='C:\Python38/chromedriver', chrome_options=options)

# ---------------------------------------------------------------------------------
# Links e variaveis
pdv_action = "http://grupogmpromo.pdvaction.com.br/"
tela_usuarios = "http://grupogmpromo.pdvaction.com.br/#/usuario-sistema/consultar"
tela_estabelecimentos = "http://grupogmpromo.pdvaction.com.br/#/estabelecimento/consultar"
tela_matriz = "http://grupogmpromo.pdvaction.com.br/#/roteiro/exportar-matriz"

# ---------------------------------------------------------------------------------
chrome.get(pdv_action)

print("request")
chrome.maximize_window()
print("maximizou")

chrome.implicitly_wait(10)

# ---------------------------------------------------------------------------------

# usuario = print(input(f'Digite o Usuário: '))
# senha = print(input(f'Digite a senha: '))



username = chrome.find_element_by_id("Username")
username.send_keys("40759530840")
password = chrome.find_element_by_id("Password")
password.send_keys("P@ssw0rd")
chrome.find_element_by_name("button").click()
chrome.implicitly_wait(10)
print("fim do login")

# ---------------------------------------------------------------------------------

os.makedirs(r'C:\testes')
chrome.find_element_by_link_text("Usuários do sistema").click()
print("clicou no usuários")
chrome.find_element_by_link_text("Gerenciar").click()
print("clicou no gerenciar")
chrome.implicitly_wait(60)

chrome.find_element_by_css_selector(".btn-primary").click()
print("clicou no exportar")
time.sleep(15)

os.rename(r'C:\testes\relatorio.xlsx', r'C:\testes\Usuários PDV.xlsx')
print("arquivo renomeado")

# ---------------------------------------------------------------------------------
# Entrou na tela de exportar estabelecimentos

# chrome.get(tela_estabelecimentos)
# # chrome.find_element_by_link_text("Estabelecimentos").click()
# print("estabelecimentos")

# chrome.find_element_by_css_selector(".btn-primary").click()
# print("clicou no exportar")

# time.sleep(15)

# os.rename(r'C:\testes\relatorio.xlsx', r'C:\testes\Estabelecimentos PDV.xlsx')
# print("arquivo renomeado")

# ---------------------------------------------------------------------------------

chrome.get(tela_matriz)
print("Entrou na tela de exportar matriz")

# ---------------------------------------------------------------------------------

print("FIMMM")

