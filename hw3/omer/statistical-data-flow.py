import sys
import time
import threading
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
import requests
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt


unit_1="BTC"
unit_2="ETH"
unit_3="USDT"

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.user_gui()

    def user_gui(self):
        self.l =QtWidgets.QLabel("Please pick your unit...")
        self.b = QtWidgets.QPushButton("Enter")

        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.addItem(unit_1)
        self.listWidget.addItem(unit_2)
        self.listWidget.addItem(unit_3)

        self.listWidget2 = QtWidgets.QListWidget()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.b)
        v_box.addWidget(self.listWidget)
        v_box.addWidget(self.listWidget2)

        self.setLayout(v_box)
        self.setWindowTitle("E-Money indexor...")

        self.listWidget.itemClicked.connect(self.baron)
        self.b.clicked.connect(self.bttnclick)

        self.show()

    def bttnclick(self):
        sender = self.sender()
        if sender.text() == "Enter":
            try:
                url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market={}-{}".format(self.listWidget.currentItem().text(),self.listWidget2.currentItem().text())
                variable = requests.get(url)
                data = variable.json()
                if data["success"] == False:
                    print("Source is not accessible!!!")
                else:
                    list1 = []
                    list2 = []
                    for i in range(len(data["result"])):
                        list1 = list1 + [data["result"][i]["TimeStamp"][11:19]]
                        list2 = list2 + [data['result'][i]["Price"]]
                    plt.plot(list1,list2)
                    plt.ylabel("Price")
                    plt.xlabel("Time - Almost 20 Minutes")
                    plt.grid(True)
                    plt.yscale('linear')
                    plt.xscale('linear')
                    plt.show()

            except:
                print("Please try to contact your developer...")


    def baron(self):
        global message
        message = self.listWidget.currentItem()
        url = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
        answer = requests.get(url)
        info = answer.json()
        if message.text() == unit_1:
            self.listWidget2.clear()
            for i in range(len(info["result"])):
                if info["result"][i]["MarketName"][0] == "B":
                    self.listWidget2.addItem(info["result"][i]["MarketName"][4:10])
        elif message.text() == unit_2:
            self.listWidget2.clear()
            for i in range(len(info["result"])):
                if info["result"][i]["MarketName"][0] == "E":
                    self.listWidget2.addItem(info["result"][i]["MarketName"][4:10])
        else:
            self.listWidget2.clear()
            for i in range(len(info["result"])):
                if info["result"][i]["MarketName"][0] == "U":
                    self.listWidget2.addItem(info["result"][i]["MarketName"][5:11])



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
