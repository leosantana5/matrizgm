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
    if moeda == "ADABTC":
        return 0
    elif moeda == "ADXBTC":
        return 0
    elif moeda == "XVSBTC":
        return 2
    elif moeda == "AEBTC":
        return 0
    elif moeda == "AGIBTC":
        return 2
    elif moeda == "AIONBTC":
        return 0
    elif moeda == "ALGOBTC":
        return 0
    elif moeda == "AMBBTC":
        return 0
    elif moeda == "ANKRBTC":
        return 0
    elif moeda == "ANTBTC":
        return 0
    elif moeda == "APPCBTC":
        return 0
    elif moeda == "ARDRBTC":
        return 0
    elif moeda == "ARKBTC":
        return 0
    elif moeda == "ARPABTC":
        return 0
    elif moeda == "ASTBTC":
        return 0
    elif moeda == "ATOMBTC":
        return 2
    elif moeda == "AVABTC":
        return 2
    elif moeda == "AVAXBTC":
        return 1
    elif moeda == "BALBTC":
        return 2
    elif moeda == "BANDBTC":
        return 1
    elif moeda == "BATBTC":
        return 0
    elif moeda == "BCDBTC":
        return 0
    elif moeda == "BCHBTC":
        return 3
    elif moeda == "BCPTBTC":
        return 0
    elif moeda == "BEAMBTC":
        return 2
    elif moeda == "BELBTC":
        return 0
    elif moeda == "BLZBTC":
        return 0
    elif moeda == "BNBBTC":
        return 2
    elif moeda == "BNTBTC":
        return 0
    elif moeda == "BQXBTC":
        return 0
    elif moeda == "BRDBTC":
        return 0
    elif moeda == "BTGBTC":
        return 2
    elif moeda == "BTSBTC":
        return 0
    elif moeda == "BZRXBTC":
        return 0
    elif moeda == "CDTBTC":
        return 0
    elif moeda == "CELRBTC":
        return 0
    elif moeda == "CHRBTC":
        return 0
    elif moeda == "CHZBTC":
        return 0
    elif moeda == "CMTBTC":
        return 0
    elif moeda == "CNDBTC":
        return 0
    elif moeda == "COMBTC":
        return 0
    elif moeda == "COMPBTC":
        return 3
    elif moeda == "COSBTC":
        return 0
    elif moeda == "COTIBTC":
        return 2
    elif moeda == "CRVBTC":
        return 0
    elif moeda == "CTSIBTC":
        return 0
    elif moeda == "CTXTBTC":
        return 0
    elif moeda == "CVCBTC":
        return 0
    elif moeda == "DASHBTC":
        return 3
    elif moeda == "DATABTC":
        return 0
    elif moeda == "DCRBTC":
        return 3
    elif moeda == "DGBBTC":
        return 0
    elif moeda == "DIABTC":
        return 2
    elif moeda == "DLTBTC":
        return 0
    elif moeda == "DNTBTC":
        return 0
    elif moeda == "DOCKBTC":
        return 0
    elif moeda == "DOGEBTC":
        return 0
    elif moeda == "DOTBTC":
        return 1
    elif moeda == "DREPBTC":
        return 0
    elif moeda == "DUSKBTC":
        return 0
    elif moeda == "EGLDBTC":
        return 3
    elif moeda == "ELFBTC":
        return 0
    elif moeda == "ENJBTC":
        return 0
    elif moeda == "EOSBTC":
        return 2
    elif moeda == "ETCBTC":
        return 2
    elif moeda == "ETHBTC":
        return 2
    elif moeda == "EVXBTC":
        return 0
    elif moeda == "FETBTC":
        return 0
    elif moeda == "FIOBTC":
        return 0
    elif moeda == "FLMBTC":
        return 0
    elif moeda == "FTMBTC":
        return 0
    elif moeda == "FTTBTC":
        return 2
    elif moeda == "FUNBTC":
        return 0
    elif moeda == "GASBTC":
        return 2
    elif moeda == "GNTBTC":
        return 0
    elif moeda == "GOBTC":
        return 0
    elif moeda == "GRSBTC":
        return 0
    elif moeda == "GTOBTC":
        return 0
    elif moeda == "GVTBTC":
        return 2
    elif moeda == "GXSBTC":
        return 0
    elif moeda == "HBARBTC":
        return 0
    elif moeda == "HCBTC":
        return 2
    elif moeda == "HIVEBTC":
        return 0
    elif moeda == "HNTBTC":
        return 2
    elif moeda == "HOTBTC":
        return 0
    elif moeda == "ICXBTC":
        return 0
    elif moeda == "IDEXBTC":
        return 0
    elif moeda == "IOSTBTC":
        return 0
    elif moeda == "IOTABTC":
        return 0
    elif moeda == "IOTXBTC":
        return 0
    elif moeda == "IRISBTC":
        return 0
    elif moeda == "JSTBTC":
        return 0
    elif moeda == "KAVABTC":
        return 0
    elif moeda == "KMDBTC":
        return 2
    elif moeda == "KNCBTC":
        return 0
    elif moeda == "KSMBTC":
        return 3
    elif moeda == "LENDBTC":
        return 0
    elif moeda == "LINKBTC":
        return 1
    elif moeda == "LOOMBTC":
        return 0
    elif moeda == "LRCBTC":
        return 0
    elif moeda == "LSKBTC":
        return 2
    elif moeda == "LTCBTC":
        return 2
    elif moeda == "LTOBTC":
        return 0
    elif moeda == "LUNABTC":
        return 0
    elif moeda == "MANABTC":
        return 0
    elif moeda == "MATICBTC":
        return 0
    elif moeda == "MBLBTC":
        return 0
    elif moeda == "MCOBTC":
        return 2
    elif moeda == "MDABTC":
        return 0
    elif moeda == "MDTBTC":
        return 0
    elif moeda == "MITHBTC":
        return 0
    elif moeda == "MKRBTC":
        return 3
    elif moeda == "MTHBTC":
        return 0
    elif moeda == "MTLBTC":
        return 0
    elif moeda == "NANOBTC":
        return 2
    elif moeda == "NASBTC":
        return 2
    elif moeda == "NAVBTC":
        return 0
    elif moeda == "NBSBTC":
            return 0
    elif moeda == "NEBLBTC":
        return 0
    elif moeda == "NEOBTC":
        return 2
    elif moeda == "NKNBTC":
        return 0
    elif moeda == "NMRBTC":
        return 3
    elif moeda == "NULSBTC":
        return 0
    elif moeda == "NXSBTC":
        return 0
    elif moeda == "OAXBTC":
        return 0
    elif moeda == "OCEANBTC":
        return 0
    elif moeda == "OGNBTC":
        return 0
    elif moeda == "OMGBTC":
        return 2
    elif moeda == "ONEBTC":
        return 0
    elif moeda == "ONGBTC":
        return 0
    elif moeda == "ONTBTC":
        return 2
    elif moeda == "ORNBTC":
        return 2
    elif moeda == "OSTBTC":
        return 0
    elif moeda == "OXTBTC":
        return 0
    elif moeda == "PAXGBTC":
        return 4
    elif moeda == "PERLBTC":
        return 0
    elif moeda == "PHBBTC":
        return 0
    elif moeda == "PIVXBTC":
        return 0
    elif moeda == "PNTBTC":
        return 0
    elif moeda == "POABTC":
        return 0
    elif moeda == "POEBTC":
        return 0
    elif moeda == "POLYBTC":
        return 0
    elif moeda == "POWRBTC":
        return 0
    elif moeda == "PPTBTC":
        return 0
    elif moeda == "QKCBTC":
        return 0
    elif moeda == "QLCBTC":
        return 0
    elif moeda == "QSPBTC":
        return 0
    elif moeda == "QTUMBTC":
        return 2
    elif moeda == "RCNBTC":
        return 0
    elif moeda == "RDNBTC":
        return 0
    elif moeda == "RENBTC":
        return 0
    elif moeda == "REPBTC":
        return 3
    elif moeda == "REQBTC":
        return 0
    elif moeda == "RLCBTC":
        return 0
    elif moeda == "RSRBTC":
        return 0
    elif moeda == "RUNEBTC":
        return 0
    elif moeda == "RVNBTC":
        return 0
    elif moeda == "SANDBTC":
        return 0
    elif moeda == "SCBTC":
        return 0
    elif moeda == "SCRTBTC":
        return 0
    elif moeda == "SKYBTC":
        return 0
    elif moeda == "SNGLSBTC":
        return 0
    elif moeda == "SNMBTC":
        return 0
    elif moeda == "SNTBTC":
        return 0
    elif moeda == "SNXBTC":
        return 2
    elif moeda == "SOLBTC":
        return 0
    elif moeda == "STEEMBTC":
        return 0
    elif moeda == "STMXBTC":
        return 0
    elif moeda == "STORJBTC":
        return 0
    elif moeda == "STPTBTC":
        return 0
    elif moeda == "STRATBTC":
        return 0
    elif moeda == "STXBTC":
        return 0
    elif moeda == "SUNBTC":
        return 3
    elif moeda == "SUSHIBTC":
        return 2
    elif moeda == "SXPBTC":
        return 0
    elif moeda == "SYSBTC":
        return 0
    elif moeda == "TCTBTC":
        return 0
    elif moeda == "TFUELBTC":
        return 0
    elif moeda == "THETABTC":
        return 0
    elif moeda == "TNBBTC":
        return 0
    elif moeda == "TOMOBTC":
        return 0
    elif moeda == "TRBBTC":
        return 3
    elif moeda == "TROYBTC":
        return 0
    elif moeda == "TRXBTC":
        return 0
    elif moeda == "UMABTC":
        return 3
    elif moeda == "UNIBTC":
        return 0
    elif moeda == "UTKBTC":
        return 0
    elif moeda == "VETBTC":
        return 0
    elif moeda == "VIABTC":
        return 0
    elif moeda == "VIBBTC":
        return 0
    elif moeda == "VIBEBTC":
        return 0
    elif moeda == "VITEBTC":
        return 0
    elif moeda == "WABIBTC":
        return 0
    elif moeda == "WANBTC":
        return 0
    elif moeda == "WAVESBTC":
        return 2
    elif moeda == "WBTCBTC":
        return 4
    elif moeda == "WINGBTC":
        return 3
    elif moeda == "WNXMBTC":
        return 3
    elif moeda == "WPRBTC":
        return 3
    elif moeda == "WRXBTC":
        return 0
    elif moeda == "WTCBTC":
        return 2
    elif moeda == "XEMBTC":
        return 0
    elif moeda == "XLMBTC":
        return 0
    elif moeda == "XMRBTC":
        return 3
    elif moeda == "XTZBTC":
        return 2
    elif moeda == "XVGBTC":
        return 0
    elif moeda == "XZCBTC":
        return 2
    elif moeda == "YFIBTC":
        return 4
    elif moeda == "YFIIBTC":
        return 4
    elif moeda == "YOYOBTC":
        return 0
    elif moeda == "ZECBTC":
        return 3
    elif moeda == "ZENBTC":
        return 2
    elif moeda == "ZILBTC":
        return 0
    elif moeda == "ZRXBTC":
        return

def MediasMoveis():
        proxies = {
                'http': 'http://85.15.179.236:4145'
            }

        velas = resposta = json.loads(requests.get(f"https://api.binance.com/api/v1/klines?symbol={moeda}&interval=1h").text)
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

          print("Moeda: " + str(moeda))
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


          sleep(1)

thread = Thread(target = Main)
thread.start()
thread.join()
