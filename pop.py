# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector

import pandas as pd
mydb = connector.connect(host="localhost", user="root", passwd="Password@123", database="reform")
mycursor = mydb.cursor(buffered=True)


class Ui_pop(object):
    def setupU(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 188)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(210, 30, 67, 17))
        self.user.setText("")
        self.user.setObjectName("user")
        self.pas = QtWidgets.QLabel(self.centralwidget)
        self.pas.setGeometry(QtCore.QRect(220, 90, 67, 17))
        self.pas.setText("")
        self.pas.setObjectName("pass")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def show(self,d,r,c):
        #self.pas.setText(d[c][r])
        self.pas.setText(d[c][r])
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_pop()
    ui.setuUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    