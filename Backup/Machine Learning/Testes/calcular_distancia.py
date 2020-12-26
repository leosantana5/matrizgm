from geopy.distance import great_circle as calcular_distancia
import requests

# API GOOGLE
api_key = 'AIzaSyAaJ4vzbbd9w7rhrYaCm7IoYhuhr8um2Eg'

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
