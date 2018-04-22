import tkinter as tk
import requests
url="https://bittrex.com/api/v1.1/public/getmarketsummaries"
response = requests.get(url)
data = response.json()
def btc_markets():
    #market listesi oluşturuluyor.
    list_btc_markets = []
    button_distance_y = 0.0
    button_distance_x = 0.0
    sliding_variable=1
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "B":
            list_btc_markets += [data["result"][i]["MarketName"]]
    #liste butonlara atanıyor.
    for i in range(len(list_btc_markets)):
        button_distance_y +=0.05
        button_btc_market_i = tk.Button(text=list_btc_markets[i][4:len(list_btc_markets[i])])
        button_btc_market_i.config(width=5)
        button_btc_market_i.config(font=("Courier", 10))
        button_btc_market_i.place(relx=0.25+button_distance_x , rely=0.0+button_distance_y)
        if i==19*sliding_variable:
            button_distance_x =0.07*sliding_variable
            button_distance_y =0.1
            sliding_variable +=1
def eth_markets():
    list_eth_markets = []
    button_distance_y = 0.0
    button_distance_x = 0.0
    sliding_variable = 1
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "E":
            list_eth_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_eth_markets)):
        button_distance_y += 0.05
        button_eth_market_i = tk.Button(text=list_eth_markets[i][4:len(list_eth_markets[i])])
        button_eth_market_i.config(width=5)
        button_eth_market_i.config(font=("Courier", 10))
        button_eth_market_i.place(relx=0.25 + button_distance_x, rely=0.0 + button_distance_y)
        if i==19*sliding_variable:
            button_distance_x =0.07*sliding_variable
            button_distance_y =0.1
            sliding_variable +=1
def usdt_markets():
    list_usdt_markets = []
    button_distance_y = 0.0
    button_distance_x = 0.0
    sliding_variable = 1
    for i in range(len(data["result"])):
        if data["result"][i]["MarketName"][0] == "U":
            list_usdt_markets += [data["result"][i]["MarketName"]]
    for i in range(len(list_usdt_markets)):
        button_distance_y += 0.05
        button_usdt_market_i = tk.Button(text=list_usdt_markets[i][5:len(list_usdt_markets[i])])
        button_usdt_market_i.config(width=5)
        button_usdt_market_i.config(font=("Courier", 10))
        button_usdt_market_i.place(relx=0.25 + button_distance_x, rely=0.0 + button_distance_y)
        if i == 19 * sliding_variable:
            button_distance_x = 0.07 * sliding_variable
            button_distance_y = 0.1
            sliding_variable += 1
screen = tk.Tk()
screen.geometry('1280x768+-9+0')

headline= tk.Label(text='MARKETS')
headline.config(width=200)
headline.config(font=("Courier", 44))
headline.pack()

button_market_1 = tk.Button(text='BTC',command=btc_markets)
button_market_1.config(width=10)
button_market_1.config(font=("Courier",30))
button_market_1.place(relx=0.015,rely=0.150)

button_market_2 = tk.Button(text='ETH',command=eth_markets)
button_market_2.config(width=10)
button_market_2.config(font=("Courier",30))
button_market_2.place(relx=0.015, rely=0.246)

button_market_3 = tk.Button(text='USDT',command=usdt_markets)
button_market_3.config(width=10)
button_market_3.config(font=("Courier",30))
button_market_3.place(relx=0.015, rely=0.342)

button_exit = tk.Button(text='EXIT', command=screen.destroy)
button_exit.config(width=5)
button_exit.config(font=("Courier",20))
button_exit.place(relx=0.92,rely=0.92)
screen.mainloop()
