import tkinter as tk
from tkinter import *
import requests
url = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
response = requests.get(url)
data = response.json()
def btc_markets():
    # market listesi oluşturuluyor.
    list_btc_markets=[]
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "B":
            list_btc_markets += [data["result"][i]["MarketName"]]
    #liste butonlara atanıyor.
    for i in range(len(list_btc_markets)):
        Lb1 = Listbox(screen)
        Lb1.insert(i,list_btc_markets[i][4:len(list_btc_markets[i])])
        Lb1.pack(side = RIGHT)
def eth_markets():
    list_eth_markets = []
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "E":
            list_eth_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_eth_markets)):
        Lb2 =Listbox(screen)
        Lb2.insert(i,list_eth_markets[i][4:len(list_eth_markets[i])])
        Lb2.pack(side=RIGHT)
def usdt_markets():
    list_usdt_markets = []
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "U":
            list_usdt_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_usdt_markets)):
        Lb3 =Listbox(screen)
        Lb3.insert(i,list_usdt_markets[i][5:len(list_usdt_markets[i])])
        Lb3.pack(side=RIGHT)
screen = tk.Tk()
screen.geometry('1280x768+-9+0')

headline= tk.Label(text='MARKETS')
headline.config(width=200)
headline.config(font=("Courier", 44))
headline.pack()

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

