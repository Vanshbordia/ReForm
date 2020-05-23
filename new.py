import mysql.connector as connector
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
mydb = connector.connect(host="localhost", user="root", passwd="Password@123", database="reform")
mycursor = mydb.cursor(buffered=True)
BLOCK_SIZE = 64
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
from PyQt5 import QtCore, QtGui, QtWidgets
def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key

def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

    
def decrypt(enc, password):
    private_key = get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

class Ui_newwindow(object):
    def __init__(self,message):
        self.message = message
    def setupUi(self, newwindow):
        newwindow.setObjectName("newwindow")
        newwindow.resize(656, 306)
        self.centralwidget = QtWidgets.QWidget(newwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 50, 271, 112))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.usrname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.usrname.setObjectName("usrname")
        self.gridLayout.addWidget(self.usrname, 1, 1, 1, 1)
        self.passwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.gridLayout.addWidget(self.passwd, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.passwd_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwd_2.setObjectName("passwd_2")
        self.gridLayout.addWidget(self.passwd_2, 0, 1, 1, 1)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(280, 200, 89, 25))
        self.add.setObjectName("add")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(280, 240, 89, 25))
        self.cancel.setObjectName("cancel")
        newwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(newwindow)
        QtCore.QMetaObject.connectSlotsByName(newwindow)

    def retranslateUi(self, newwindow):
        _translate = QtCore.QCoreApplication.translate
        newwindow.setWindowTitle(_translate("newwindow", "New Account"))
        self.label_2.setText(_translate("newwindow", "Password"))
        self.label.setText(_translate("newwindow", "Username"))
        self.label_3.setText(_translate("newwindow", "Site"))
        self.add.setText(_translate("newwindow", "Add Site"))
        self.cancel.setText(_translate("newwindow", "Cancel"))
        self.add.clicked.connect(self.addn)
        self.cancel.clicked.connect(self.closeEvent)
        global password
        password = self.message

    
    def addn(self):
        
        s= self.passwd_2.text()
        u = self.usrname.text()
        p=self.passwd.text()
        qry ="insert into {} values('{}','{}','{}')"
        mycursor.execute((qry.format(self.message,s,u,p)))
        mydb.commit()
        
    def closeEvent(self):
        QtWidgets.MainWindow.instance().quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newwindow = QtWidgets.QMainWindow()
    ui = Ui_newwindow()
    ui.setupUi(newwindow)
    newwindow.show()
    sys.exit(app.exec_())
