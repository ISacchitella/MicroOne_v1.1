# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inserisci_metri_cubi_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inserisci_Metri_Cubi_Window(object):
    def setupUi(self, Inserisci_Metri_Cubi_Window):
        Inserisci_Metri_Cubi_Window.setObjectName("Inserisci_Metri_Cubi_Window")
        Inserisci_Metri_Cubi_Window.resize(274, 112)
        Inserisci_Metri_Cubi_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(Inserisci_Metri_Cubi_Window)
        self.label_5.setGeometry(QtCore.QRect(-20, -10, 531, 41))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Inserisci_Metri_Cubi_Window)
        self.label.setGeometry(QtCore.QRect(90, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 140, 255);")
        self.label.setObjectName("label")
        self.cancel_btn_ = QtWidgets.QPushButton(Inserisci_Metri_Cubi_Window)
        self.cancel_btn_.setGeometry(QtCore.QRect(0, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cancel_btn_.setFont(font)
        self.cancel_btn_.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"                 color: rgb(255, 255, 255);\n"
"                 border-radius:10px;\n"
"             ")
        self.cancel_btn_.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cancel/res/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn_.setIcon(icon)
        self.cancel_btn_.setObjectName("cancel_btn_")
        self.avanti_btn = QtWidgets.QPushButton(Inserisci_Metri_Cubi_Window)
        self.avanti_btn.setGeometry(QtCore.QRect(180, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.avanti_btn.setFont(font)
        self.avanti_btn.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.avanti_btn.setObjectName("avanti_btn")
        self.metri_cubi_spinBox = QtWidgets.QSpinBox(Inserisci_Metri_Cubi_Window)
        self.metri_cubi_spinBox.setGeometry(QtCore.QRect(10, 40, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.metri_cubi_spinBox.setFont(font)
        self.metri_cubi_spinBox.setStyleSheet("QSpinBox::down-button {\n"
"\n"
"        image: url(:/arrows/res/down_arrow.png);\n"
"        width:50px;\n"
"\n"
"\n"
"        }\n"
"\n"
"\n"
"        QSpinBox::up-button {\n"
"\n"
"\n"
"        image: url(:/arrows/res/up_arrow.png);\n"
"        width: 50px;\n"
"        }\n"
"\n"
"\n"
"        QSpinBox {\n"
"        color: rgb(0, 0, 0);\n"
"        border-radius:25px;\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(0,140,255);\n"
"\n"
"\n"
"        }")
        self.metri_cubi_spinBox.setWrapping(False)
        self.metri_cubi_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.metri_cubi_spinBox.setReadOnly(False)
        self.metri_cubi_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.metri_cubi_spinBox.setMinimum(1)
        self.metri_cubi_spinBox.setMaximum(3000)
        self.metri_cubi_spinBox.setObjectName("metri_cubi_spinBox")
        self.keyboard_btn = QtWidgets.QPushButton(Inserisci_Metri_Cubi_Window)
        self.keyboard_btn.setGeometry(QtCore.QRect(160, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keyboard_btn.setFont(font)
        self.keyboard_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.keyboard_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/keyboard/res/keyboard_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.keyboard_btn.setIcon(icon1)
        self.keyboard_btn.setObjectName("keyboard_btn")

        self.retranslateUi(Inserisci_Metri_Cubi_Window)
        self.cancel_btn_.clicked.connect(Inserisci_Metri_Cubi_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Inserisci_Metri_Cubi_Window)

    def retranslateUi(self, Inserisci_Metri_Cubi_Window):
        _translate = QtCore.QCoreApplication.translate
        Inserisci_Metri_Cubi_Window.setWindowTitle(_translate("Inserisci_Metri_Cubi_Window", "Metri Cubi"))
        self.label.setText(_translate("Inserisci_Metri_Cubi_Window", "Inserisci Metri Cubi"))
        self.avanti_btn.setText(_translate("Inserisci_Metri_Cubi_Window", "Riepilogo"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inserisci_Metri_Cubi_Window = QtWidgets.QWidget()
    ui = Ui_Inserisci_Metri_Cubi_Window()
    ui.setupUi(Inserisci_Metri_Cubi_Window)
    Inserisci_Metri_Cubi_Window.show()
    sys.exit(app.exec_())
