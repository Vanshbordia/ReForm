from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import mysql.connector as connector
from PyQt5.QtWidgets import QDialog
mydb = connector.connect(host="localhost", user="root", passwd="Password@123", database="reform")
mycursor = mydb.cursor(buffered=True)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self,message):
        self.message = message
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(687, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 190, 131, 71))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 60, 271, 112))
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

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.add)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Site"))

    def add(self):
        s= self.passwd_2.text()
        u = self.usrname.text()
        p= self.passwd.text()
        qry ="insert into {} values('{}','{}','{}')"
        mycursor.execute(qry.format(self.message,s,u,p))
        mydb.commit()
    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
