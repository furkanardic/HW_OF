import matplotlib
matplotlib.use('TkAgg')#grafik penceresi
import tkinter as tk
from tkinter import *
import requests
import matplotlib.pyplot as plt

url = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
response = requests.get(url)
data = response.json()
btc=0
eth=0
usdt=0
market=""
money=""
prices=[]
times=[]
def scale():#grafiği çizdiriyoruz.
    global market
    global money
    global times
    global prices
    title=market+" / "+money
    plt.title(title)
    plt.ylabel("Currency")
    plt.xlabel("Time")
    plt.grid(True)
    plt.plot(times, prices)
    plt.show()
def graph_datas():#grafik değerlerini x ve y koordinatlarını ayrı ayrı olarak listeye atıyor.
    try:
        global market
        global money
        market = Lb4.get("active")
        money = Lb1.get("active")
        global prices
        global times
        url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market={}-{}".format(market, money)
        response = requests.get(url)
        data = response.json()
        for i in range(len(data["result"])):
            prices += [data["result"][i]["Price"]]
            times += [data["result"][i]["TimeStamp"][11:19]]
        #grafiği çizdiriyoruz.
        scale()
    except:
        error = tk.Label(text='Please firstly choose the market and push the search.')
        error.config(width=200)
        error.config(font=("Courier", 15))
        error.pack()
def markets():#2.listeleri bastırıyor.
    if (Lb4.get("active")=="BTC")and(btc==0)and(eth==0)and(usdt==0):
        btc_markets()
    elif (Lb4.get("active")=="ETH")and(btc==0)and(eth==0)and(usdt==0):
        eth_markets()

    elif (Lb4.get("active")=="USDT")and(btc==0)and(eth==0)and(usdt==0):
        usdt_markets()
def btc_markets():
    global btc
    btc=1
    # market listesi oluşturuluyor.
    list_btc_markets=[]
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "B":
            list_btc_markets += [data["result"][i]["MarketName"]]
    #liste listboxa kopyalanıyor.

    for i in range(len(list_btc_markets)):
        Lb1.insert(i,list_btc_markets[i][4:len(list_btc_markets[i])])
    Lb1.config(width=8)#en'i ayarlanıyor.
    Lb1.config(font=("Courier", 20))
    Lb1.pack(side=LEFT , fill=BOTH)#sola yapıştırıp , tamamını dolduruyor.
def eth_markets():
    global eth
    eth=1
    list_eth_markets = []
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "E":
            list_eth_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_eth_markets)):
        Lb1.insert(i,list_eth_markets[i][4:len(list_eth_markets[i])])
    Lb1.config(width=8)
    Lb1.config(font=("Courier",20))
    Lb1.pack(side=LEFT , fill=BOTH)
def usdt_markets():
    global usdt
    usdt=1
    list_usdt_markets = []
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "U":
            list_usdt_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_usdt_markets)):
        Lb1.insert(i,list_usdt_markets[i][5:len(list_usdt_markets[i])])
    Lb1.config(width=8)
    Lb1.config(font=("Courier",20))
    Lb1.pack(side=LEFT , fill=BOTH)
screen = tk.Tk()
screen.geometry('1280x768+-9+0')
Lb1 = Listbox(screen)

headline= tk.Label(text='MARKETS')
headline.config(width=200)
headline.config(font=("Courier", 44))
headline.pack()

button_search = tk.Button(screen, text="SEARCH", command=markets)
button_search.config(width=7)
button_search.config(font=("Courier",20))
button_search.place(relx=0.01,rely=0.01)

button_search_currency = tk.Button(screen, text="SEARCH CURRENCY", command=graph_datas)
button_search_currency.config(width=20)
button_search_currency.config(font=("Courier", 20))
button_search_currency.place(relx=0.12, rely=0.01)

button_exit = tk.Button(text='EXIT', command=screen.destroy)
button_exit.config(width=5)
button_exit.config(font=("Courier",20))
button_exit.place(relx=0.92,rely=0.92)

Lb4 = Listbox(screen)
Lb4.insert(1,"BTC")
Lb4.insert(2,"ETH")
Lb4.insert(3,"USDT")
Lb4.config(width=7)#en
Lb4.config(font=("Courier",25))
Lb4.pack(side=LEFT , fill=BOTH)

screen.mainloop()