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

class Ui_loginwindow(object):
    
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(515, 370)
        self.centralwidget = QtWidgets.QWidget(loginwindow)
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
        self.loginb = QtWidgets.QPushButton(self.centralwidget)
        self.loginb.setGeometry(QtCore.QRect(220, 210, 88, 27))
        self.loginb.setObjectName("loginb")
        loginwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "Login"))
        self.label.setText(_translate("loginwindow", "Username"))
        self.label_2.setText(_translate("loginwindow", "Password"))
        self.loginb.setText(_translate("loginwindow", "Login"))
        self.loginb.clicked.connect(self.click)
    
    def click(self):
        global usr
        usr = self.usrname.text()
        psw = self.passwd.text()
        qry="Select * from users where username = '{}'"
        mycursor.execute(qry.format(usr))
        s=mycursor.fetchall()
    
        p1=s[0][1]
        
        for i in string.ascii_letters:
            w=psw+i
            
            j=sha3.sha3_512(w.encode('utf-8')).hexdigest()
            
            if j == p1:
                
                self.tableclick(usr)
                
                return usr
                
        mydb.commit

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
    loginwindow = QtWidgets.QMainWindow()
    ui = Ui_loginwindow()
    ui.setupUi(loginwindow)
    loginwindow.show()
    sys.exit(app.exec_())
