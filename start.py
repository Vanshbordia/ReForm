from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_loginwindow
from signup import Ui_signupwindow

class Ui_Dialog(object):
    def logind(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_loginwindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()
    def signupd(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_signupwindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()
    def setupUi(self, Dialog):
        Dialog.setObjectName("ReForm")
        Dialog.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 150, 184, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("ReForm", "ReForm"))
        self.pushButton.setText(_translate("ReForm", "Login"))
        self.pushButton.clicked.connect(self.logind)
        self.pushButton_2.setText(_translate("ReForm", "Sign Up"))
        self.pushButton_2.clicked.connect(self.signupd)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
