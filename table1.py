from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from new import Ui_newwindow
mydb = connector.connect(host="localhost", user="root", passwd="Password@123", database="reform")
mycursor = mydb.cursor(buffered=True)

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_MainWindow(object):
    def __init__(self,message):
        
        self.message = message
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 20, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(810, 60, 89, 25))
        self.refresh.setObjectName("refresh")
        self.usernamel = QtWidgets.QLabel(self.centralwidget)
        self.usernamel.setGeometry(QtCore.QRect(810, 460, 100, 17))
        self.usernamel.setText("")
        self.usernamel.setObjectName("usernamel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "New"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.usernamel.setText(self.message)
        self.refresh.clicked.connect(self.upda)
        self.upda()
        self.tableView.clicked.connect(self.func)
        self.pushButton.clicked.connect(self.new)
    
    def func(self,item):
        po=QMessageBox()
        r=item.column()
        c=item.row()
        po.setWindowTitle("User")
        po.setText(str(df[r+1][c]))
        
        po.exec_()

    def new(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_newwindow(self.message)
        self.ui.setupUi(self.window)
        self.window.show()
    
    def upda(self):
        global df
        qry ="select * from {}"
        mycursor.execute(qry.format(self.message))
        global r
        r=mycursor.fetchall()
        df=pd.DataFrame(r)
        ddf = df.iloc[:,:2]
        model=pandasModel(ddf)
        self.tableView.setModel(model)
        self.tableView.update()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
