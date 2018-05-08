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
            url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market={}-{}".format(self.value1, self.value2)
            variable = requests.get(url)
            data = variable.json()
            time.sleep(1)

class process(threading.Thread):
    def __init__(self,data):
        threading.Thread.__init__(self)
        self.data = data
    def run(self):

        if self.data["success"] == False:
            print("Source is not accessible!!!")
        else:
            list1 = []
            list2 = []
            for i in range(len(self.data["result"])):
                list1 = list1 + [self.data["result"][i]["TimeStamp"][11:19]]
                list2 = list2 + [self.data['result'][i]["Price"]]


def zoom_factory(ax,base_scale = 2.):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*.5
        xdata = event.xdata # get event x location
        ydata = event.ydata # get event y location
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1/base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
        # set new limits
        ax.set_xlim([xdata - cur_xrange*scale_factor,
                     xdata + cur_xrange*scale_factor])
        ax.set_ylim([ydata - cur_yrange*scale_factor,
                     ydata + cur_yrange*scale_factor])
        plt.draw() # force re-draw

    fig = ax.get_figure() # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event',zoom_fun)

    #return the function
    return zoom_fun


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
                thread2 = process(self.data)
                thread.start()
                thread.join()
                thread2.start()
                thread2.join()
                plt.plot(self.list1, self.list2)
                plt.ylabel("Price")
                plt.xlabel("Time - Almost 20 Minutes")
                plt.grid(True)
                plt.yscale('linear')
                plt.xscale('linear')
                plt.show()
                scale = 1.5
                zoom_factory(plt,base_scale=scale)
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