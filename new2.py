from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import mysql.connector as connector

mydb = connector.connect(host="localhost", user="root", passwd="Password@123", database="reform")
mycursor = mydb.cursor(buffered=True)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def add(self):
        s= self.passwd_2.text()
        u = self.usrname.text()
        p= self.passwd.text()
        qry ="insert into {} values('{}','{}','{}')"
        mycursor.execute(qry.format(self.message,s,u,p))
        mydb.commit()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 279)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 30, 271, 112))
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
        self.passwd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_2.setObjectName("passwd_2")
        self.gridLayout.addWidget(self.passwd_2, 0, 1, 1, 1)
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(290, 180, 89, 25))
        self.add.setObjectName("add")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(290, 220, 89, 25))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Site"))
        self.add.setText(_translate("Form", "Add SIte"))
        self.cancel.setText(_translate("Form", "Add SIte"))
        self.add.clicked.connect(self.add)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
