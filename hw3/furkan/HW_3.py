import tkinter as tk
from tkinter import *
import requests
url = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
response = requests.get(url)
data = response.json()
def btc_markets():
    top = Tk()
    # market listesi oluşturuluyor.
    list_btc_markets=[]
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "B":
            list_btc_markets += [data["result"][i]["MarketName"]]
    #liste butonlara atanıyor.
    for i in range(len(list_btc_markets)):
        Lb1 = Listbox(top)
        Lb1.insert(i,list_btc_markets[i][4:len(list_btc_markets[i])])
        Lb1.pack()
    top.mainloop()
def eth_markets():

    top = Tk()
    list_eth_markets = []
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "E":
            list_eth_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_eth_markets)):
        Lb2 =Listbox(top)
        Lb2.insert(i,list_eth_markets[i][4:len(list_eth_markets[i])])
        Lb2.pack()
    top.mainloop()
def usdt_markets():
    top = Tk()
    list_usdt_markets = []
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "U":
            list_usdt_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_usdt_markets)):
        Lb2 =Listbox(top)
        Lb2.insert(i,list_usdt_markets[i][5:len(list_usdt_markets[i])])
        Lb2.pack()
    top.mainloop()
screen = tk.Tk()
screen.geometry('1280x768+-9+0')

headline= tk.Label(text='MARKETS')
headline.config(width=200)
headline.config(font=("Courier", 44))
headline.pack()


button_market_1 = tk.Button(text='BTC', command=btc_markets)
button_market_1.config(width=10)
button_market_1.config(font=("Courier",30))
button_market_1.place(relx=0.015,rely=0.150)

button_market_2 = tk.Button(text='ETH', command=eth_markets)
button_market_2.config(width=10)
button_market_2.config(font=("Courier",30))
button_market_2.place(relx=0.015, rely=0.246)

button_market_3 = tk.Button(text='USDT', command=usdt_markets)
button_market_3.config(width=10)
button_market_3.config(font=("Courier",30))
button_market_3.place(relx=0.015, rely=0.342)

button_exit = tk.Button(text='EXIT', command=screen.destroy)
button_exit.config(width=5)
button_exit.config(font=("Courier",20))
button_exit.place(relx=0.92,rely=0.92)
screen.mainloop()

