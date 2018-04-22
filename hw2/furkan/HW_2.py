import requests
market=input("Please give market name(btc-etc-usdt):")
money=input("Please give money unit:")
try:
    url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market={}-{}".format(market,money)
    response = requests.get(url)
    data = response.json()
    print("1 {} is {} {}".format(money ,data["result"][0]["Last"],market ))
except:
    print("Please give useble market and money name.")
