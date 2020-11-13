# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registra_prodotti.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reg_prodotto_Window(object):
    def setupUi(self, Reg_prodotto_Window):
        Reg_prodotto_Window.setObjectName("Reg_prodotto_Window")
        Reg_prodotto_Window.resize(480, 320)
        Reg_prodotto_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome_label = QtWidgets.QLabel(Reg_prodotto_Window)
        self.nome_label.setGeometry(QtCore.QRect(142, 60, 196, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.nome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_label.setObjectName("nome_label")
        self.nome_textbox = QtWidgets.QLineEdit(Reg_prodotto_Window)
        self.nome_textbox.setGeometry(QtCore.QRect(52, 90, 376, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nome_textbox.setFont(font)
        self.nome_textbox.setStyleSheet("border-radius:30px;\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(0,140,255);\n"
"")
        self.nome_textbox.setObjectName("nome_textbox")
        self.data_scad_label = QtWidgets.QLabel(Reg_prodotto_Window)
        self.data_scad_label.setGeometry(QtCore.QRect(140, 0, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.data_scad_label.setFont(font)
        self.data_scad_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.data_scad_label.setObjectName("data_scad_label")
        self.save_btn = QtWidgets.QPushButton(Reg_prodotto_Window)
        self.save_btn.setGeometry(QtCore.QRect(400, 280, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.save_btn.setObjectName("save_btn")
        self.label_5 = QtWidgets.QLabel(Reg_prodotto_Window)
        self.label_5.setGeometry(QtCore.QRect(-10, 0, 501, 31))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Reg_prodotto_Window)
        self.label.setGeometry(QtCore.QRect(360, 40, 41, 31))
        self.label.setStyleSheet("image: url(:/icons/res/prodotto_icon.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.cancel_btn_ = QtWidgets.QPushButton(Reg_prodotto_Window)
        self.cancel_btn_.setGeometry(QtCore.QRect(390, 0, 71, 31))
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
        self.concentrazione_label = QtWidgets.QLabel(Reg_prodotto_Window)
        self.concentrazione_label.setGeometry(QtCore.QRect(142, 170, 196, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.concentrazione_label.setFont(font)
        self.concentrazione_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.concentrazione_label.setAlignment(QtCore.Qt.AlignCenter)
        self.concentrazione_label.setObjectName("concentrazione_label")
        self.concentrazione_spinBox = QtWidgets.QSpinBox(Reg_prodotto_Window)
        self.concentrazione_spinBox.setGeometry(QtCore.QRect(170, 210, 151, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.concentrazione_spinBox.setFont(font)
        self.concentrazione_spinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.concentrazione_spinBox.setStyleSheet("QSpinBox::down-button {\n"
"\n"
"                    image: url(:/arrows/res/down_arrow.png);\n"
"                    width:50px;\n"
"                    }\n"
"\n"
"\n"
"                    QSpinBox::up-button {\n"
"\n"
"                    image: url(:/arrows/res/up_arrow.png);\n"
"                    width: 50px;\n"
"                    }\n"
"\n"
"\n"
"                    QSpinBox {\n"
"                    color: rgb(0, 0, 0);\n"
"                \n"
"    background-color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(0,140,255);\n"
"                    border-radius:30px;\n"
"\n"
"\n"
"                    }\n"
"                ")
        self.concentrazione_spinBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.concentrazione_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.concentrazione_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.concentrazione_spinBox.setMinimum(1)
        self.concentrazione_spinBox.setMaximum(3000)
        self.concentrazione_spinBox.setSingleStep(1)
        self.concentrazione_spinBox.setProperty("value", 1)
        self.concentrazione_spinBox.setObjectName("concentrazione_spinBox")
        self.data_scad_dateEdit = QtWidgets.QDateEdit(Reg_prodotto_Window)
        self.data_scad_dateEdit.setEnabled(False)
        self.data_scad_dateEdit.setGeometry(QtCore.QRect(150, 10, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.data_scad_dateEdit.setFont(font)
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
        self.data_scad_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 10, 1), QtCore.QTime(0, 0, 0)))
        self.data_scad_dateEdit.setObjectName("data_scad_dateEdit")
        self.keyboard_btn = QtWidgets.QPushButton(Reg_prodotto_Window)
        self.keyboard_btn.setGeometry(QtCore.QRect(0, 270, 81, 31))
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
        self.pushButton = QtWidgets.QPushButton(Reg_prodotto_Window)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 171, 28))
        self.pushButton.setStyleSheet("image: url(:/microone_logo/res/Microne Bianco.png);\n"
"background-color: rgb(0, 140, 255);")
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.data_scad_dateEdit.raise_()
        self.nome_label.raise_()
        self.nome_textbox.raise_()
        self.data_scad_label.raise_()
        self.save_btn.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.cancel_btn_.raise_()
        self.concentrazione_label.raise_()
        self.concentrazione_spinBox.raise_()
        self.keyboard_btn.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Reg_prodotto_Window)
        self.cancel_btn_.clicked.connect(Reg_prodotto_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Reg_prodotto_Window)

    def retranslateUi(self, Reg_prodotto_Window):
        _translate = QtCore.QCoreApplication.translate
        Reg_prodotto_Window.setWindowTitle(_translate("Reg_prodotto_Window", "Registra Prodotto"))
        self.nome_label.setText(_translate("Reg_prodotto_Window", "Inserisci nome Prodotto"))
        self.data_scad_label.setText(_translate("Reg_prodotto_Window", "Inserisci data di scadenza"))
        self.save_btn.setText(_translate("Reg_prodotto_Window", "Salva"))
        self.concentrazione_label.setText(_translate("Reg_prodotto_Window", "Concentrazione"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reg_prodotto_Window = QtWidgets.QWidget()
    ui = Ui_Reg_prodotto_Window()
    ui.setupUi(Reg_prodotto_Window)
    Reg_prodotto_Window.show()
    sys.exit(app.exec_())
