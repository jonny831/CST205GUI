from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys 


class SecondPage(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainPage,self).__init__()
		uic.loadUi('SecondPage', self)

	