# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Output_essay = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Output_essay.setGeometry(QtCore.QRect(200, 60, 381, 371))
        self.Output_essay.setObjectName("Output_essay")
        self.essay_completion_text = QtWidgets.QPushButton(self.centralwidget)
        self.essay_completion_text.setGeometry(QtCore.QRect(290, 10, 181, 32))
        self.essay_completion_text.setObjectName("essay_completion_text")
        self.Thankyou_text = QtWidgets.QLabel(self.centralwidget)
        self.Thankyou_text.setGeometry(QtCore.QRect(260, 450, 241, 51))
        self.Thankyou_text.setObjectName("Thankyou_text")
        self.Goback_button = QtWidgets.QPushButton(self.centralwidget)
        self.Goback_button.setGeometry(QtCore.QRect(10, 520, 113, 32))
        self.Goback_button.setObjectName("Goback_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 22))
        self.menubar.setObjectName("menubar")
        self.menuMain_Window = QtWidgets.QMenu(self.menubar)
        self.menuMain_Window.setObjectName("menuMain_Window")
        MainWindow.setMenuBar(self.menubar)
        self.NewFile = QtWidgets.QAction(MainWindow)
        self.NewFile.setObjectName("NewFile")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuMain_Window.addAction(self.NewFile)
        self.menuMain_Window.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuMain_Window.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.essay_completion_text.setText(_translate("MainWindow", "Here Is Your Essay!"))
        self.Thankyou_text.setText(_translate("MainWindow", "Thank you for using EassayWritter.com\n"
"                                 :)"))
        self.Goback_button.setText(_translate("MainWindow", "Go back"))
        self.menuMain_Window.setTitle(_translate("MainWindow", "File"))
        self.NewFile.setText(_translate("MainWindow", "New"))
        self.NewFile.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As.."))
