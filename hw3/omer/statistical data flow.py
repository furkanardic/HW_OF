import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.user_gui()

    def user_gui(self):
        self.l =QtWidgets.QLabel("Please enter your units...")
        self.le = QtWidgets.QLineEdit()
        self.le2 = QtWidgets.QLineEdit()
        self.b = QtWidgets.QPushButton("Enter")
        self.b2 = QtWidgets.QPushButton("Clear")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.le)
        v_box.addWidget(self.le2)
        v_box.addWidget(self.b)
        v_box.addWidget(self.b2)

        self.setLayout(v_box)
        self.setWindowTitle("E-Money indexor...")

        self.b.clicked.connect(self.bttnclick)
        self.b2.clicked.connect(self.bttnclick)

        self.show()

    def bttnclick(self):
        sender = self.sender()
        if sender.text() == "Enter":
            print(self.le.text())
        else:
            self.le.clear()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())