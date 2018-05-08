import sys
import time
import threading
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
import requests
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

exitFlag = 0
unit_1="BTC"
unit_2="ETH"
unit_3="USDT"

class refresh(threading.Thread):
    def __init__(self, value1, value2):
        threading.Thread.__init__(self)
        self.value1 = value1
        self.value2 = value2
    def run(self):
        while 1:
            self.url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market={}-{}".format(self.value1, self.value2)
            self.variable = requests.get(self.url)
            self.data = self.variable.json()
            if self.data["success"] == False:
                print("Source is not accessible!!!")
            else:
                self.list1 = []
                self.list2 = []
                self.list1.clear()
                self.list2.clear()
                for i in range(len(self.data["result"])):
                    self.list1 = self.list1 + [self.data["result"][i]["TimeStamp"][11:19]]
                    self.list2 = self.list2 + [self.data['result'][i]["Price"]]
                    plt.plot(self.list1, self.list2)
            time.sleep(1)


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.user_gui()

    def user_gui(self):
        self.l =QtWidgets.QLabel("   E-Money Indexor...\nPlease pick your unit...")
        self.b = QtWidgets.QPushButton("Enter")

        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.addItem(unit_1)
        self.listWidget.addItem(unit_2)
        self.listWidget.addItem(unit_3)
        self.listWidget.setFixedSize(75, 200)

        self.listWidget2 = QtWidgets.QListWidget()
        self.listWidget2.setFixedSize(75, 200)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.listWidget)
        h_box2.addWidget(self.listWidget2)
        h_box2.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addWidget(self.b)
        v_box.addLayout(h_box2)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("E-Money indexor...")

        self.listWidget.itemClicked.connect(self.baron)
        self.b.clicked.connect(self.bttnclick)

        self.show()

    def bttnclick(self):
        sender = self.sender()
        if sender.text() == "Enter":
            try:
                thread = refresh(self.listWidget.currentItem().text(), self.listWidget2.currentItem().text())
                thread.start()
                plt.ylabel("Price")
                plt.xlabel("Time - Almost 20 Minutes")
                plt.grid(True)
                plt.yscale('linear')
                plt.xscale('linear')
                plt.show()
            except:
                self.l.setText("Please try to contact your developer...")


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


#self.listWidget.currentItem().text()
#self.listWidget2.currentItem().text()