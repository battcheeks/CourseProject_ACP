

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(276, 90)
        OtherWindow.move(420,257)
        OtherWindow.setStyleSheet(" background-color:rgb(0, 85, 127) ;")
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 39, 251, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
        self.pushButton.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_3.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_2.setStyleSheet(" background-color: rgb(170, 170, 255);")


        self.pushButton.clicked.connect(lambda:self.on_click())
        self.pushButton_2.clicked.connect(lambda:self.on_click1())
        self.pushButton_3.clicked.connect(lambda:self.on_click2())

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Choose Tracker"))
        self.pushButton.setText(_translate("OtherWindow", "csrt"))
        self.pushButton_2.setText(_translate("OtherWindow", "kcf"))
        self.pushButton_3.setText(_translate("OtherWindow", "mosse"))
        self.label.setText(_translate("OtherWindow", "Choose the tracker "))
        '''self.pushButton.clicked.connect(self.on_click())
        self.pushButton_2.clicked.connect(self.on_click1())
        self.pushButton_3.clicked.connect(self.on_click2())'''
    def on_click(self):
        print("Executing csrt Tracking")
        exec (open("csrt.py").read())
    def on_click1(self):
        print("Executing kcf Tracking")
        exec (open("kcf.py").read())

    def on_click2(self):
        print("Executing mosse Tracking")
        exec (open("mosse.py").read())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
