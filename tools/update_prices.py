import requests

def get_price_shares(tiker):
    URL = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/"+\
          tiker+\
          ".jsonp?iss.meta=off&iss.json=extended&lang=ru&iss.only=marketdata,securities"

    req = requests.get(url=URL)
    data = req.json()

    if len(data[1]["marketdata"]) == 0:
        return
    return data[1]["marketdata"][0]["LAST"]

def get_price_ETF(tiker):
    URL = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQTF/securities/"+\
          tiker+\
          ".jsonp?iss.meta=off&iss.only=marketdata&iss.json=extended&lang=ru"

    req = requests.get(url=URL)
    data = req.json()

    if len(data[1]["marketdata"]) == 0:
        return
    return data[1]["marketdata"][0]["LAST"]

def check_asset(tiker):
    price = get_price_shares(tiker)
    if price == None:
        price = get_price_ETF(tiker)
        if price == None:
            return
    return price