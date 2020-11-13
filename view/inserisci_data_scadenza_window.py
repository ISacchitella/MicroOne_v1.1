# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inserisci_data_scadenza_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inserisci_Data_Scadenza_Window(object):
    def setupUi(self, Inserisci_Data_Scadenza_Window):
        Inserisci_Data_Scadenza_Window.setObjectName("Inserisci_Data_Scadenza_Window")
        Inserisci_Data_Scadenza_Window.resize(480, 320)
        Inserisci_Data_Scadenza_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(Inserisci_Data_Scadenza_Window)
        self.label_5.setGeometry(QtCore.QRect(-20, -10, 531, 41))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Inserisci_Data_Scadenza_Window)
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
        self.cancel_btn_ = QtWidgets.QPushButton(Inserisci_Data_Scadenza_Window)
        self.cancel_btn_.setGeometry(QtCore.QRect(390, 0, 81, 31))
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
        self.avanti_btn = QtWidgets.QPushButton(Inserisci_Data_Scadenza_Window)
        self.avanti_btn.setGeometry(QtCore.QRect(340, 240, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.avanti_btn.setFont(font)
        self.avanti_btn.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.avanti_btn.setObjectName("avanti_btn")
        self.data_scad_dateEdit = QtWidgets.QDateEdit(Inserisci_Data_Scadenza_Window)
        self.data_scad_dateEdit.setEnabled(True)
        self.data_scad_dateEdit.setGeometry(QtCore.QRect(140, 90, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.data_scad_dateEdit.setFont(font)
        self.data_scad_dateEdit.setTabletTracking(False)
        self.data_scad_dateEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.data_scad_dateEdit.setStyleSheet("QDateEdit::down-button {\n"
"\n"
"\n"
"     image: url(:/arrows/res/down_arrow.png);\n"
"     width:50px;\n"
"\n"
"\n"
"     }\n"
"\n"
"\n"
"     QDateEdit::up-button {\n"
"\n"
"\n"
"     image: url(:/arrows/res/up_arrow.png);\n"
"     width: 50px;\n"
"     }\n"
"\n"
"\n"
"     QDateEdit {\n"
"     color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"     border-radius:25px;\n"
"border: 5px solid rgb(0,140,255);\n"
"\n"
"\n"
"}")
        self.data_scad_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.data_scad_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 10, 1), QtCore.QTime(0, 0, 0)))
        self.data_scad_dateEdit.setObjectName("data_scad_dateEdit")
        self.keyboard_btn = QtWidgets.QPushButton(Inserisci_Data_Scadenza_Window)
        self.keyboard_btn.setGeometry(QtCore.QRect(150, 170, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keyboard_btn.setFont(font)
        self.keyboard_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"image: url(:/keyboard/res/keyboard_icon.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.keyboard_btn.setText("")
        self.keyboard_btn.setFlat(False)
        self.keyboard_btn.setObjectName("keyboard_btn")
        self.pushButton = QtWidgets.QPushButton(Inserisci_Data_Scadenza_Window)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 171, 28))
        self.pushButton.setStyleSheet("image: url(:/microone_logo/res/Microne Bianco.png);\n"
"background-color: rgb(0, 140, 255);")
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label_5.raise_()
        self.cancel_btn_.raise_()
        self.avanti_btn.raise_()
        self.data_scad_dateEdit.raise_()
        self.keyboard_btn.raise_()
        self.pushButton.raise_()
        self.label.raise_()

        self.retranslateUi(Inserisci_Data_Scadenza_Window)
        self.cancel_btn_.clicked.connect(Inserisci_Data_Scadenza_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Inserisci_Data_Scadenza_Window)

    def retranslateUi(self, Inserisci_Data_Scadenza_Window):
        _translate = QtCore.QCoreApplication.translate
        Inserisci_Data_Scadenza_Window.setWindowTitle(_translate("Inserisci_Data_Scadenza_Window", "Data Scadenza"))
        self.label.setText(_translate("Inserisci_Data_Scadenza_Window", "Inserisci Data di scadenza"))
        self.avanti_btn.setText(_translate("Inserisci_Data_Scadenza_Window", "Avanti"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inserisci_Data_Scadenza_Window = QtWidgets.QWidget()
    ui = Ui_Inserisci_Data_Scadenza_Window()
    ui.setupUi(Inserisci_Data_Scadenza_Window)
    Inserisci_Data_Scadenza_Window.show()
    sys.exit(app.exec_())
