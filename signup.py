# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sha3
import random
import hashlib
import string
import Crypto
import mysql.connector as connector
from Crypto.Cipher import AES
mydb = connector.connect(host="localhost", user="root", passwd="Password@123", database="reform")
mycursor = mydb.cursor()
from table1 import Ui_MainWindow

class Ui_signupwindow(object):
    def setupUi(self, signupwindow):
        signupwindow.setObjectName("signupwindow")
        signupwindow.resize(515, 370)
        self.centralwidget = QtWidgets.QWidget(signupwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 120, 271, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.usrname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.usrname.setObjectName("usrname")
        self.gridLayout.addWidget(self.usrname, 0, 1, 1, 1)
        self.passwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.gridLayout.addWidget(self.passwd, 1, 1, 1, 1)
        self.signupb = QtWidgets.QPushButton(self.centralwidget)
        self.signupb.setGeometry(QtCore.QRect(220, 210, 88, 27))
        self.signupb.setObjectName("signupb")
        signupwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(signupwindow)
        QtCore.QMetaObject.connectSlotsByName(signupwindow)

    def retranslateUi(self, signupwindow):
        _translate = QtCore.QCoreApplication.translate
        signupwindow.setWindowTitle(_translate("signupwindow", "Signup"))
        self.label.setText(_translate("signupwindow", "Username"))
        self.label_2.setText(_translate("signupwindow", "Password"))
        self.signupb.setText(_translate("signupwindow", "Signup"))
        self.signupb.clicked.connect(self.click)


    def click(self):
        usr = self.usrname.text()
        psw = self.passwd.text()
        
        pep=random.choice(string.ascii_letters)
        pepas=psw+pep
        print(pepas)
        pepas=sha3.sha3_512(pepas.encode('utf-8')).hexdigest()
        print(pepas)
        
        qry="insert into users values('{}','{}',0)"
        cruqry="CREATE TABLE {} (site VARCHAR(100) NOT NULL,username VARCHAR(100) NOT NULL,password VARCHAR(1024) NOT NULL);"
        mycursor.execute(qry.format(usr,pepas))
        mycursor.execute(cruqry.format(usr))
        mycursor.close()
        mydb.commit()
        self.tableclick(usr)

    def tableclick(self,usr):   
        self.window = QtWidgets.QMainWindow()
        self.message =usr
        self.window.hide()
        self.ui = Ui_MainWindow(self.message)
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signupwindow = QtWidgets.QMainWindow()
    ui = Ui_signupwindow()
    ui.setupUi(signupwindow)
    signupwindow.show()
    sys.exit(app.exec_())
