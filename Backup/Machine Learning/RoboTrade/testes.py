import math

from binance.client import Client
from statistics import mean
from datetime import datetime
from threading import Thread
from time import sleep
import os
import requests
import json
import pywhatkit
from keyboard import press
import decimal
from binance.websockets import BinanceSocketManager
ctx = decimal.Context()
ctx.prec = 8


# ----------- Horario atual  --------- #
now = datetime.now()
hora = now.hour
minuto = now.minute+1

print(f'Programa Iniciado - {hora}:{now.minute}\n')

#kit.sendwhatmsg(telefone, "Mensagem enviada", hora, minuto)




# ------------ Keys da API ---------------- #

telefone = "+5511943483056"

client = Client('fEwODVjVhj3K5OsWGXxVoPbWquEQtY7KO1b9JtD4TIIzSLtMDHCGfceZ56gQsnqS', 'XQUOCuavHTwyFmmkoVS9zjvNdnoEjGvz6rpkEEqIBxaa2F3s3yWu2cVnU3FmGd2i')

time_res = client.get_server_time()


balanc = client.get_asset_balance(asset='BTC')
if (balanc is None):
    input("Não Existe Saldo Disponível em BTC, Aperte Qualquer Tecla para Finalizar")
    exit(0)

info = client.get_account()
balance = ctx.create_decimal(balanc["free"])

print("Saldos da Carteira\n")
for infos in info:
     balances = info["balances"]
     print(balances)
     print(infos)
     for paresBalance in balances:
          if float(paresBalance["free"]) > 0:
               print(f'{paresBalance["asset"]} - {paresBalance["free"]}')
     break
print("\n \b")

saldo25 = (balance/100)*25
saldo50 = (balance/100)*50
saldo75 = (balance/100)*75
saldoTotal = balance



moeda = "BLZBTC"

tickers = client.get_orderbook_tickers()

for i in tickers:
    symbol = i["symbol"]
    bidPrice = i["bidPrice"]
    bidQty = i["bidQty"]
    askPrice = i["askPrice"]
    askQty = str(i["askQty"])

    btc = 1

    p = (btc / float(askPrice))

    # if float(askQty) <= 0.02:
    # print(f"Moeda;{symbol};Preço compra;{bidPrice};Qtd compra;{bidQty};Preço Venda;{askPrice};Qtd Venda;({askQty})")

    if symbol == "ADABTC":
        print(f"Moeda - {symbol},Preço Venda {askPrice}, Qtd Venda {askQty}, {p}")




