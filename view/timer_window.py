# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Timer_Window(object):
    def setupUi(self, Timer_Window):
        Timer_Window.setObjectName("Timer_Window")
        Timer_Window.resize(480, 320)
        Timer_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.description_label = QtWidgets.QLabel(Timer_Window)
        self.description_label.setGeometry(QtCore.QRect(30, 83, 420, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.description_label.setObjectName("description_label")
        self.timer_label = QtWidgets.QLabel(Timer_Window)
        self.timer_label.setGeometry(QtCore.QRect(70, 140, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.timer_label.setFont(font)
        self.timer_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.timer_label.setTextFormat(QtCore.Qt.AutoText)
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timer_label")
        self.label_5 = QtWidgets.QLabel(Timer_Window)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"image: url(:/sfondo_microone/res/pagina_MICROONE.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.cancel_btn = QtWidgets.QPushButton(Timer_Window)
        self.cancel_btn.setEnabled(False)
        self.cancel_btn.setGeometry(QtCore.QRect(390, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"                 color: rgb(255, 255, 255);\n"
"                 border-radius:10px;\n"
"             ")
        self.cancel_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cancel/res/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon)
        self.cancel_btn.setObjectName("cancel_btn")
        self.download_btn = QtWidgets.QPushButton(Timer_Window)
        self.download_btn.setEnabled(False)
        self.download_btn.setGeometry(QtCore.QRect(170, 0, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.download_btn.setFont(font)
        self.download_btn.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"                 color: rgb(255, 255, 255);\n"
"                 border-radius:10px;\n"
"             ")
        self.download_btn.setObjectName("download_btn")
        self.poweroff_btn = QtWidgets.QPushButton(Timer_Window)
        self.poweroff_btn.setGeometry(QtCore.QRect(10, 40, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.poweroff_btn.setFont(font)
        self.poweroff_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"image: url(:/poweroff /res/poweroff_icon.png);")
        self.poweroff_btn.setText("")
        self.poweroff_btn.setObjectName("poweroff_btn")
        self.pushButton = QtWidgets.QPushButton(Timer_Window)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 171, 28))
        self.pushButton.setStyleSheet("image: url(:/microone_logo/res/Microne Bianco.png);\n"
"background-color: rgb(0, 140, 255);")
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Timer_Window)
        self.label.setGeometry(QtCore.QRect(195, 0, 210, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.download_btn.raise_()
        self.label_5.raise_()
        self.description_label.raise_()
        self.timer_label.raise_()
        self.cancel_btn.raise_()
        self.poweroff_btn.raise_()
        self.pushButton.raise_()
        self.label.raise_()

        self.retranslateUi(Timer_Window)
        self.cancel_btn.clicked.connect(Timer_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Timer_Window)

    def retranslateUi(self, Timer_Window):
        _translate = QtCore.QCoreApplication.translate
        Timer_Window.setWindowTitle(_translate("Timer_Window", "Timer"))
        self.description_label.setText(_translate("Timer_Window", "ALLONTANARSI"))
        self.timer_label.setText(_translate("Timer_Window", "10"))
        self.download_btn.setText(_translate("Timer_Window", "Download"))
        self.label.setText(_translate("Timer_Window", "Trattamento in Corso"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Timer_Window = QtWidgets.QWidget()
    ui = Ui_Timer_Window()
    ui.setupUi(Timer_Window)
    Timer_Window.show()
    sys.exit(app.exec_())
