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
last_xlim=[]
last_ylim=[]

class ZoomPan:
    def __init__(self):
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None

    def zoom_factory(self, ax, base_scale=2.):
        def zoom(event):
            global last_xlim, last_ylim
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata  # get event x location
            ydata = event.ydata  # get event y location

            if event.button == 'down':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'up':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
            #         print event.button

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])
            
            last_xlim=[xdata - new_width * (1 - relx), xdata + new_width * (relx)]
            last_ylim=[ydata - new_height * (1 - rely), ydata + new_height * (rely)]

            ax.set_xlim(last_xlim)
            ax.set_ylim(last_ylim)
            ax.figure.canvas.draw()

        fig = ax.get_figure()  # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure()  # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event', onPress)
        fig.canvas.mpl_connect('button_release_event', onRelease)
        fig.canvas.mpl_connect('motion_notify_event', onMotion)

        # return the function
        return onMotion

class refresh(threading.Thread):
    def __init__(self, value1, value2):
        threading.Thread.__init__(self)
        self.value1 = value1
        self.value2 = value2
        self.fig = plt.figure()
    def run(self):
        scale = 1.1
        zp = ZoomPan()
        global last_xlim, last_ylim
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
                plt.clf()
                plt.grid(False)
                plt.plot(self.list1, self.list2)
                plt.ylabel("Price")
                plt.xlabel("Time - Almost 20 Minutes")
                plt.grid(True)
                plt.yscale('linear')
                plt.xscale('linear')
                if last_xlim != [] and last_ylim!=[]:
                    print(last_xlim)
                    print(last_ylim)
                    plt.xlim(last_xlim)
                    plt.ylim(last_ylim)
                plt.xticks(rotation=20)
                plt.draw()
                zp.zoom_factory(plt.gca(), base_scale=scale)
                #zp.pan_factory(plt.gca())
                #plt.pause(0.1)

            time.sleep(1)



class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
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
                scale = 1.1
                zp = ZoomPan()
                plt.clf()
                plt.ylabel("Price")
                plt.xlabel("Time - Almost 20 Minutes")
                plt.grid(True)
                zp.zoom_factory(plt.gca(), base_scale=scale)
                #zp.pan_factory(plt.gca())
                plt.xticks(rotation=20)
                plt.show()
                self.thread = refresh(self.listWidget.currentItem().text(), self.listWidget2.currentItem().text())
                self.thread.start()

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