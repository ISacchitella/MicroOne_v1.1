# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inserisci_lotto_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inserisci_Lotto_Window(object):
    def setupUi(self, Inserisci_Lotto_Window):
        Inserisci_Lotto_Window.setObjectName("Inserisci_Lotto_Window")
        Inserisci_Lotto_Window.resize(480, 320)
        Inserisci_Lotto_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(Inserisci_Lotto_Window)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"image: url(:/sfondo_lotto/res/pagina_MICROONE_ins_lotto.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.cancel_btn_ = QtWidgets.QPushButton(Inserisci_Lotto_Window)
        self.cancel_btn_.setGeometry(QtCore.QRect(410, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cancel_btn_.setFont(font)
        self.cancel_btn_.setStyleSheet("background-color: rgb(0, 134, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"                 color: rgb(255, 255, 255);\n"
"             \n"
"background-color: rgb(0, 134, 255);")
        self.cancel_btn_.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cancel/res/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn_.setIcon(icon)
        self.cancel_btn_.setFlat(True)
        self.cancel_btn_.setObjectName("cancel_btn_")
        self.avanti_btn = QtWidgets.QPushButton(Inserisci_Lotto_Window)
        self.avanti_btn.setGeometry(QtCore.QRect(340, 240, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.avanti_btn.setFont(font)
        self.avanti_btn.setStyleSheet("background-color: rgb(0, 134, 255);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.avanti_btn.setObjectName("avanti_btn")
        self.lotto_textbox = QtWidgets.QLineEdit(Inserisci_Lotto_Window)
        self.lotto_textbox.setGeometry(QtCore.QRect(100, 40, 280, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lotto_textbox.setFont(font)
        self.lotto_textbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lotto_textbox.setStyleSheet("border-radius:30px;\n"
"                    background-color: rgb(0, 0, 0);\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    border: 5px solid rgb(0, 134, 255);\n"
"                ")
        self.lotto_textbox.setText("")
        self.lotto_textbox.setObjectName("lotto_textbox")
        self.keyboard_btn = QtWidgets.QPushButton(Inserisci_Lotto_Window)
        self.keyboard_btn.setGeometry(QtCore.QRect(10, 235, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keyboard_btn.setFont(font)
        self.keyboard_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/keyboard/res/keyboard.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.keyboard_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/keyboard/res/keyboard_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.keyboard_btn.setIcon(icon1)
        self.keyboard_btn.setObjectName("keyboard_btn")

        self.retranslateUi(Inserisci_Lotto_Window)
        self.cancel_btn_.clicked.connect(Inserisci_Lotto_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Inserisci_Lotto_Window)

    def retranslateUi(self, Inserisci_Lotto_Window):
        _translate = QtCore.QCoreApplication.translate
        Inserisci_Lotto_Window.setWindowTitle(_translate("Inserisci_Lotto_Window", "Lotto"))
        self.avanti_btn.setText(_translate("Inserisci_Lotto_Window", "Avanti"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inserisci_Lotto_Window = QtWidgets.QWidget()
    ui = Ui_Inserisci_Lotto_Window()
    ui.setupUi(Inserisci_Lotto_Window)
    Inserisci_Lotto_Window.show()
    sys.exit(app.exec_())
