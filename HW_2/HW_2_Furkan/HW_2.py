import requests
market=input("Please write a market name(BTC-ETH-USDT)")
currency=input("Please write a currecy(Ex: BitCoin => Btc )")
try :
    url="https://bittrex.com/api/v1.1/public/getmarketsummary?market={}-{}".format(market,currency)
    response = requests.get(url)
    data=response.json()
    print("At the moment,The answer for this convertion ({}---{}) is {}({}/{}) ".format(market,currency,data["result"][0]["Last"],market,currency))
except TypeError:
    print("Please write VALID market or currency id.\n")











#print(data["result"][0]["Last"])
#print(type(data["result"][0]))
##veri=data["result"][0]
##for i in veri:
##  print(data["result"][0][i])
#response = requests.get("http://api.open-notify.org/astros.json")
#data = response.json()


