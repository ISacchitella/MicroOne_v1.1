# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seleziona_prodotto_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Seleziona_Prodotto_Window(object):
    def setupUi(self, Seleziona_Prodotto_Window):
        Seleziona_Prodotto_Window.setObjectName("Seleziona_Prodotto_Window")
        Seleziona_Prodotto_Window.resize(480, 320)
        Seleziona_Prodotto_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prodotti_comboBox = QtWidgets.QComboBox(Seleziona_Prodotto_Window)
        self.prodotti_comboBox.setGeometry(QtCore.QRect(87, 40, 376, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.prodotti_comboBox.setFont(font)
        self.prodotti_comboBox.setStyleSheet("QComboBox::down-arrow {\n"
"\n"
"    image: url(:/arrows/res/down_arrow.png);\n"
"        width: 14px;\n"
"        height: 14px;\n"
"\n"
"        }\n"
"        QComboBox::drop-down\n"
"        {\n"
"        border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"        color:black\n"
"\n"
"        }\n"
"\n"
"QComboBox {\n"
"    color: black;\n"
"border-radius:30px;\n"
"border: 5px solid rgb(0, 134, 255);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.prodotti_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.prodotti_comboBox.setObjectName("prodotti_comboBox")
        self.label_5 = QtWidgets.QLabel(Seleziona_Prodotto_Window)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"image: url(:/sfondo_sel_prodotto/res/pagina_MICROONE_selezione_prodotto.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Seleziona_Prodotto_Window)
        self.label_2.setGeometry(QtCore.QRect(17, 40, 60, 60))
        self.label_2.setStyleSheet("image: url(:/hand/res/Hand.png);\n"
"      border: 5px solid rgb(0, 134, 255);\n"
"border-radius:30px;\n"
"     ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.cancel_btn_1 = QtWidgets.QPushButton(Seleziona_Prodotto_Window)
        self.cancel_btn_1.setGeometry(QtCore.QRect(390, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cancel_btn_1.setFont(font)
        self.cancel_btn_1.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"                    color: rgb(255, 255, 255);\n"
"                    border-radius:10px;\n"
"                ")
        self.cancel_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cancel/res/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn_1.setIcon(icon)
        self.cancel_btn_1.setObjectName("cancel_btn_1")
        self.cancel_btn_ = QtWidgets.QPushButton(Seleziona_Prodotto_Window)
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
        self.cancel_btn_.setIcon(icon)
        self.cancel_btn_.setFlat(True)
        self.cancel_btn_.setObjectName("cancel_btn_")
        self.avanti_btn = QtWidgets.QPushButton(Seleziona_Prodotto_Window)
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
        self.cancel_btn_1.raise_()
        self.label_5.raise_()
        self.prodotti_comboBox.raise_()
        self.label_2.raise_()
        self.cancel_btn_.raise_()
        self.avanti_btn.raise_()

        self.retranslateUi(Seleziona_Prodotto_Window)
        self.cancel_btn_.clicked.connect(Seleziona_Prodotto_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Seleziona_Prodotto_Window)

    def retranslateUi(self, Seleziona_Prodotto_Window):
        _translate = QtCore.QCoreApplication.translate
        Seleziona_Prodotto_Window.setWindowTitle(_translate("Seleziona_Prodotto_Window", "Prodotto"))
        self.avanti_btn.setText(_translate("Seleziona_Prodotto_Window", "Avanti"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Seleziona_Prodotto_Window = QtWidgets.QWidget()
    ui = Ui_Seleziona_Prodotto_Window()
    ui.setupUi(Seleziona_Prodotto_Window)
    Seleziona_Prodotto_Window.show()
    sys.exit(app.exec_())
