
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWind(object):
    def setupUi(self, OtherWind):
        OtherWind.setObjectName("OtherWind")
        OtherWind.resize(500, 100)
        self.centralwidget = QtWidgets.QWidget(OtherWind)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 100, 75))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 10, 200, 75))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 10, 100, 75))
        self.pushButton_3.setObjectName("pushButton_3")
        OtherWind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        OtherWind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWind)
        self.statusbar.setObjectName("statusbar")
        OtherWind.setStatusBar(self.statusbar)
        OtherWind.setStyleSheet(" background-color:rgb(0, 85, 127) ;")
        self.pushButton.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_3.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_2.setStyleSheet(" background-color: rgb(170, 170, 255);")

        self.retranslateUi(OtherWind)
        QtCore.QMetaObject.connectSlotsByName(OtherWind)

    def retranslateUi(self, OtherWind):
        _translate = QtCore.QCoreApplication.translate
        OtherWind.setWindowTitle(_translate("OtherWind", "MainWindow"))
        self.pushButton.setText(_translate("OtherWind", "Gamma Filter"))
        self.pushButton_2.setText(_translate("OtherWind", "Segmentation Connected Components"))
        self.pushButton_3.setText(_translate("OtherWind", "Blurring filters"))
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_3.clicked.connect(self.on_click3)
    def on_click(self):
        print("Starting Code for Gamma Imaging")
        exec (open("gammaCorrection.py").read())
    def on_click2(self):
        print("Starting Segmentation for Image using Connected Components Analysis")
        exec (open("segmentation.py").read())
    def on_click3(self):
        print("Blurring filters using Kernels and Functions")
        exec (open("filter.py").read())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWind = QtWidgets.QMainWindow()
    ui = Ui_OtherWind()
    ui.setupUi(OtherWind)
    OtherWind.show()
    sys.exit(app.exec_())
