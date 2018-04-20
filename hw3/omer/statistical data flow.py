import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    label1 = QtWidgets.QLabel(w)
    label1.setText("Coming Soon...")
    w.setWindowTitle("Statical Data Flow v1.0")
    w.setGeometry(500,300,500,500)
    label1.move(250,100)
    w.show()
    sys.exit(app.exec_())
    

window()
