
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys 


class MainPage(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainPage,self).__init__()
		uic.loadUi('MainWindow.ui',self)
		


app = QtWidgets.QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())

