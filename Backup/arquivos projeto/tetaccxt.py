import math

from binance.client import Client
from statistics import mean
from datetime import datetime
from threading import Thread
from time import sleep
import os
import requests
import json
import pymongo
import uuid

import pywhatkit
from keyboard import press
import decimal
from binance.websockets import BinanceSocketManager
ctx = decimal.Context()
ctx.prec = 8

# ------------------------------------------------------------- Horario atual  --------- #
clear = lambda: os.system('cls')
now = datetime.now()
hora = now.hour
minuto = now.minute+1

mes2 = now.month-1

dia = now.day
mes = now.month
ano = now.year
hora = now.hour
mes = now.month
segundo = now.second
diadehj = f'{dia} {mes} {ano}'
noventadias = f'{dia} {mes2} {ano}'
diaamericano = f'{ano}-{mes}-{dia} {hora}:{minuto}:{segundo}'

myclient = pymongo.MongoClient("mongodb://localhost")
mydb = myclient["RoboTrade"]
mycol = mydb["Velas"]

# --------------------------------------------------------- Keys da API ---------------- #
import datetime

#client = Client('gjvgUAYVNDWUqL5hgqt2EVJyrJQ0ccIdpEv45mCWj6gxNN42tUxZ26IGz4ZJZZ3l', '592molyoe5UccdxBSrbbOP5h5fgrUC8YGFbfyfTv2TpavGnoc9DXoDuefMQKUkUy') #Prod
client = Client('fEwODVjVhj3K5OsWGXxVoPbWquEQtY7KO1b9JtD4TIIzSLtMDHCGfceZ56gQsnqS', 'XQUOCuavHTwyFmmkoVS9zjvNdnoEjGvz6rpkEEqIBxaa2F3s3yWu2cVnU3FmGd2i') #Elias
# client = Client('56OhgEi35UbkDYdvftOtst4641MxI5O6SiY4sB0ZagbdFc9XrqW0200TatbEpuFe', 'PLE3XYirbpNEzTTJ1tnXAoFmuFmcz160yBnfNA3zyDdnklZkU8IZ9O6I6NQ3OwF5') Teste Homologação

server = client.get_system_status()
status = server.get("status")

if (status != 0):
    exit(-1)

time_res = client.get_server_time() #Horario do servidor

servertime = (datetime.datetime.fromtimestamp(time_res["serverTime"]/1000))

print(f'Programa Iniciado - {hora}:{now.minute}')
print(f'Horário do servidor - {servertime.hour}:{servertime.minute}\n')

# ---------------------------------------- Saldo da carteira - Balance ---------------- #
balanc = client.get_asset_balance(asset='BTC')

if (balanc is None):
    input("Não Existe Saldo Disponível em BTC, Aperte Qualquer Tecla para Finalizar")
    exit(0)

info = client.get_account()
balance = ctx.create_decimal(balanc["free"])

print("Saldos da Carteira\n")
for infos in info:
     balances = info["balances"]
     for paresBalance in balances:
          if float(paresBalance["free"]) > 0:
               print(f'{paresBalance["asset"]} - {paresBalance["free"]}')
     break
print("\n \b")

saldo25 = (balance/100)*25
saldo50 = (balance/100)*50
saldo75 = (balance/100)*75
saldoTotal = balance

# ----------------------------------------------------- Moeda ---------------------- #
moeda = input("Digite o par da moeda a ser trabalhada: ").upper()
dadosMoeda = client.get_symbol_info(moeda)
filtros = dadosMoeda.get("filters")
dadosLotSize = filtros[2]
valorLotSize = dadosLotSize.get("minQty")[0:1]

ultimasOrdens = None
verde = None
amarelo = None

#websocket
def ProcessamentoVelas(resposta):
    k = resposta["k"]
    c = k["c"]
    s = k["s"]
    t = k["T"]

    mycol.insert_one({"CloseTime": c, "Symbol": s, "EndTime": t})

def DeletarMoedas():
    mycol.delete_many({"Symbol": moeda})

#bm = BinanceSocketManager(client)
#bm.start_kline_socket(moeda, ProcessamentoVelas)
#bm.start()
#fimwebsocket


def CasasDecimaisMoeda():
    if moeda == "WINGBTC":
        return 3
    elif moeda == "CRVBTC":
        return 2
    elif moeda == "SXPBTC":
        return 0
    elif moeda == "TRXBTC":
        return 0

def MediasMoveis():
        proxies = {
                  'http': 'http://45.70.204.245:4145',
                  'https': 'https://45.70.204.245:4145'
                 }

        velas = resposta = json.loads(requests.get(f"https://api.binance.com/api/v1/klines?symbol={moeda}&interval=1h",
                                                   proxies=proxies).text)
        # velas = client.get_historical_klines(moeda, Client.KLINE_INTERVAL_1HOUR, diadehj)

        maVERDE = velas[-7:]
        maAMARELO = velas[-25:]
        verdes = []
        amarelos = []

        for i in maVERDE:
             verdes.append(ctx.create_decimal(i[4]))

        for i in maAMARELO:
             amarelos.append(ctx.create_decimal(i[4]))

        return mean(verdes), mean(amarelos)

def ObterPicoMaximo(ordemCorrente):
     dataUltimaOrdem = ordemCorrente["time"]
     dataUltimaOrdemFormatada = (datetime.datetime.fromtimestamp(dataUltimaOrdem / 1000))
     dataCorrente = now - dataUltimaOrdemFormatada
     segundos = dataCorrente.total_seconds()
     minutos = segundos / 60

     tempo = "1m"
     if (minutos >= 1000):
        tempo = "1h"

     resposta = json.loads(requests.get(f"https://api.binance.com/api/v1/klines?symbol={moeda}&interval={tempo}&limit=1000&startTime={dataUltimaOrdem}").text)

     valores = []
     datas = []

     for i in resposta:
         datas.append(float(i[0]))
         valores.append(float(i[2]))

     picoMaximo = max(valores)
     indiceMaximo = valores.index(max(valores))
     dataMaxima = (datetime.datetime.fromtimestamp(datas[indiceMaximo]/1000))

     return picoMaximo

def Main():
     while (True):
          ultimasOrdens = None
          myorders = client.get_all_orders(symbol=moeda, limit=10)
          myorders = list(filter(lambda x: x.get("status") != "CANCELED" and x.get("status") != "NEW", myorders))

          if len(myorders) > 0:
             ultimasOrdens = myorders[len(myorders) - 1]

          verde, amarelo = MediasMoveis()
          moedas = client.get_all_tickers()
          moedaCorrente = list(filter(lambda x: x.get("symbol") == moeda, moedas))
          valorMoeda = ctx.create_decimal(moedaCorrente[0].get("price"))

          valorMoeda25 = round(((balance / valorMoeda) / 100) * 25, CasasDecimaisMoeda())
          valorMoeda100 = round((balance / valorMoeda), CasasDecimaisMoeda())


          picoMaximo = None
          doisPorCento = None
          valorStoplossDois = None
          tresPorCento = None
          valorStoplossTres = None

          if len(myorders) > 0:
               picoMaximo = ObterPicoMaximo(ultimasOrdens)

               doisPorCento = (picoMaximo / 100) * 2
               valorStoplossDois = picoMaximo - doisPorCento
               valorStoplossDois = ctx.create_decimal(valorStoplossDois)

               tresPorCento = (picoMaximo / 100) * 3
               valorStoplossTres = picoMaximo - tresPorCento
               valorStoplossTres = ctx.create_decimal(valorStoplossTres)

          clear()

          # asks = venda
          # bids = compra
          ordensDisponiveis = client.get_order_book(symbol=moeda)
          ultimasOrdensVenda = ordensDisponiveis.get("asks")
          menorValorOrdemVenda = ultimasOrdensVenda[2]
          valorOrdemVenda = menorValorOrdemVenda[0]

          ultimasOrdensCompra = ordensDisponiveis.get("bids")
          maiorValorOrdemCompra = ultimasOrdensCompra[2]
          valorOrdemCompra = maiorValorOrdemCompra[0]

          print("Verde: " + str(verde))
          print("Amarelo: " + str(amarelo))
          print("Valor Moeda: " + str(valorMoeda))
          print("Menor Valor Venda: " + str(valorOrdemVenda))
          print("Maior Valor Compra: " + str(valorOrdemCompra))
          print("Pico Máximo: " + str(picoMaximo))
          print("Hash: " + str(uuid.uuid4()))

          #DeletarMoedas()

          if verde > amarelo:
               if (ultimasOrdens is None) or (ultimasOrdens["side"] == "SELL" and ultimasOrdens["type"] == "LIMIT" and ultimasOrdens["status"] == "FILLED"):
                      ordemCompra = client.create_order(symbol=moeda,
                                                        side=Client.SIDE_BUY,
                                                        type=Client.ORDER_TYPE_LIMIT,
                                                        timeInForce=Client.TIME_IN_FORCE_GTC,
                                                        price=valorOrdemVenda,
                                                        quantity=valorMoeda25)

               elif (ultimasOrdens["side"] == "BUY" and ultimasOrdens["type"] == "LIMIT" and ultimasOrdens["status"] == "FILLED"):
                      if valorMoeda < valorStoplossTres:
                              ordemVendaStopLoss = client.create_oco_order(symbol=moeda,
                                                                           side=Client.SIDE_SELL,
                                                                           type=Client.ORDER_TYPE_STOP_LOSS_LIMIT,
                                                                           timeInForce=Client.TIME_IN_FORCE_GTC,
                                                                           price=valorOrdemCompra,
                                                                           quantity=valorMoeda100,
                                                                           stopPrice=valorStoplossDois,
                                                                           stopLimitPrice=valorStoplossTres)

               elif (ultimasOrdens["side"] == "SELL" and ultimasOrdens["type"] == "STOP-LIMIT" and ultimasOrdens["status"] == "FILLED"):
                    if valorMoeda > ultimasOrdens["price"]:
                         ordemCompra = client.create_order(symbol=moeda,
                                                           side=Client.SIDE_BUY,
                                                           type=Client.ORDER_TYPE_LIMIT,
                                                           timeInForce=Client.TIME_IN_FORCE_GTC,
                                                           price=valorOrdemVenda,
                                                           quantity=valorMoeda25)

          else:

               if ultimasOrdens is not None:
                   if (ultimasOrdens["side"] == "BUY" and ultimasOrdens["type"] == "LIMIT" and ultimasOrdens["status"] == "FILLED"):
                       ordemCompra = client.create_order(symbol=moeda,
                                                         side=Client.SIDE_SELL,
                                                         type=Client.ORDER_TYPE_LIMIT,
                                                         timeInForce=Client.TIME_IN_FORCE_GTC,
                                                         price=valorOrdemCompra,
                                                         quantity=valorMoeda100)#PRECISA VENDER COM 100 POR CENTO


          sleep(0.1)

thread = Thread(target = Main)
thread.start()
thread.join()
