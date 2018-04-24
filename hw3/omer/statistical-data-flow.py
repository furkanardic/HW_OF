import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
import requests


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.user_gui()

    def user_gui(self):
        self.l =QtWidgets.QLabel("Please pick your unit...")
        self.b = QtWidgets.QPushButton("Enter")

        listWidget = QListWidget()
        ls = ['BTC', 'ETH', 'USDT','EXIT']
        listWidget.addItems(ls)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.b)
        v_box.addWidget(listWidget)

        self.setLayout(v_box)
        self.setWindowTitle("E-Money indexor...")

        self.b.clicked.connect(self.bttnclick)

        self.show()

    def bttnclick(self):
        sender = self.sender()
        if sender.text() == "Enter":
            try:
                url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market={}-{}".format(self.le.text(),self.le2.text())
                variable = requests.get(url)
                data = variable.json()
                if data["success"] == False:
                    print("Your selections are not accessible.Try another money units or write units in capital letters.\nFor example\nWrong: btc \\ True: BTC")
                else:
                    print("Value = {}",data['result'][0])
            except:
                print("Please try to contact your developer...")


        else:
            self.le.clear()
            self.le2.clear()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
