from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import Ui_OtherWindow
from acpx import Ui_OtherWind
from PyQt5.QtWidgets import QWidget,QPushButton,QInputDialog,QLineEdit,QApplication

class Ui_MainWindow(object):
    def openWind(self):
        self.wind=QtWidgets.QMainWindow()
        self.ui= Ui_OtherWind()
        self.ui.setupUi(self.wind)
        self.wind.show()
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(" background-color:rgb(0,85,127) ;")
        MainWindow.resize(507, 405)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 221, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 70, 221, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 130, 221, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 221, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 250, 221, 50))
        icon = QtGui.QIcon.fromTheme("\\")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setObjectName("pushButton_5")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(-60, 470, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 10, 256, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 310, 221, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Color Thresholding using OpenCV"))
        self.pushButton_2.setText(_translate("MainWindow", "Shape detection using OpenCV"))
        self.pushButton_3.setText(_translate("MainWindow", "Detection using haar-cascade"))
        self.pushButton_4.setText(_translate("MainWindow", "Hough Lines detection"))
        self.pushButton_5.setText(_translate("MainWindow", "Filters in OpenCV and their effect on images"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Course Project</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">This is our Course project for the subject Advanced Computer Programming it is based on the features of Computer Vision or OpenCV and how it makes our lives easier.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Tracking using OpenCV"))
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_3.clicked.connect(self.on_click3)
        self.pushButton_4.clicked.connect(self.on_click4)
        self.pushButton_5.clicked.connect(self.openWind)
        self.pushButton_6.clicked.connect(self.openWindow)
        self.pushButton.setStyleSheet(" background-color: rgb(150, 170, 245);")
        self.pushButton_3.setStyleSheet(" background-color: rgb(150, 170, 245);")
        self.pushButton_2.setStyleSheet(" background-color: rgb(150, 170, 245);")
        self.pushButton_4.setStyleSheet(" background-color: rgb(150, 170, 245);")
        self.pushButton_5.setStyleSheet(" background-color: rgb(150, 170, 245);")
        self.pushButton_6.setStyleSheet(" background-color: rgb(150, 170, 245);")

    def on_click(self):
        print("Starting Code for Color Thresholding")
        exec (open("ct.py").read())
    def on_click2(self):
        print("Starting Shape Detection for the given Input image")
        exec (open("detect_shapes.py").read())
    def on_click3(self):
        print("Starting Face Detection using Haar-Cascade")
        exec (open("face.py").read())
    def on_click4(self):
        print("Starting Striaght line Detection using Hough-Lines")
        import cv2 as cv
        import numpy as np
        import matplotlib.pyplot as plt

        def do_canny(frame):
            gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            blur = cv.GaussianBlur(gray, (5, 5), 0)
            canny = cv.Canny(blur, 50, 150)
            return canny

        def do_segment(frame):
            height = frame.shape[0]

            polygons = np.array([
                [(0, height), (800, height), (380, 290)]
            ])

            mask = np.zeros_like(frame)

            cv.fillPoly(mask, polygons, 255)

            segment = cv.bitwise_and(frame, mask)
            return segment

        def calculate_lines(frame, lines):
            left = []
            right = []

            for line in lines:
                # Reshapes line from 2D array to 1D array
                x1, y1, x2, y2 = line.reshape(4)
                # Fits a linear polynomial to the x and y coordinates and returns a vector of coefficients which describe the slope and y-intercept
                parameters = np.polyfit((x1, x2), (y1, y2), 1)
                slope = parameters[0]
                y_intercept = parameters[1]
                # If slope is negative, the line is to the left of the lane, and otherwise, the line is to the right of the lane
                if slope < 0:
                    left.append((slope, y_intercept))
                else:
                    right.append((slope, y_intercept))
            # Averages out all the values for left and right into a single slope and y-intercept value for each line
            left_avg = np.average(left, axis=0)
            right_avg = np.average(right, axis=0)
            # Calculates the x1, y1, x2, y2 coordinates for the left and right lines
            left_line = calculate_coordinates(frame, left_avg)
            right_line = calculate_coordinates(frame, right_avg)
            return np.array([left_line, right_line])

        def calculate_coordinates(frame, parameters):
            slope, intercept = parameters
            # Sets initial y-coordinate as height from top down (bottom of the frame)
            y1 = frame.shape[0]
            # Sets final y-coordinate as 150 above the bottom of the frame
            y2 = int(y1 - 150)
            # Sets initial x-coordinate as (y1 - b) / m since y1 = mx1 + b
            x1 = int((y1 - intercept) / slope)
            # Sets final x-coordinate as (y2 - b) / m since y2 = mx2 + b
            x2 = int((y2 - intercept) / slope)
            return np.array([x1, y1, x2, y2])

        def visualize_lines(frame, lines):
            # Creates an image filled with zero intensities with the same dimensions as the frame
            lines_visualize = np.zeros_like(frame)
            # Checks if any lines are detected
            if lines is not None:
                for x1, y1, x2, y2 in lines:
                    # Draws lines between two coordinates with green color and 5 thickness
                    cv.line(lines_visualize, (x1, y1), (x2, y2), (0, 255, 0), 5)
            return lines_visualize

        # The video feed is read in as a VideoCapture object
        cap = cv.VideoCapture("input.mp4")
        while (cap.isOpened()):
            # ret = a boolean return value from getting the frame, frame = the current frame being projected in the video
            ret, frame = cap.read()
            canny = do_canny(frame)
            cv.imshow("canny", canny)
            # plt.imshow(frame)
            # plt.show()
            segment = do_segment(canny)
            hough = cv.HoughLinesP(segment, 2, np.pi / 180, 100, np.array([]), minLineLength=100, maxLineGap=50)

            lines = calculate_lines(frame, hough)
            # Visualizes the lines
            lines_visualize = visualize_lines(frame, lines)
            cv.imshow("hough", lines_visualize)

            output = cv.addWeighted(frame, 0.9, lines_visualize, 1, 1)

            cv.imshow("output", output)

            if cv.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
