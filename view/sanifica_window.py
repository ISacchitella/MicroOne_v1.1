# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sanifica_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sanifica_Window(object):
    def setupUi(self, Sanifica_Window):
        Sanifica_Window.setObjectName("Sanifica_Window")
        Sanifica_Window.resize(480, 320)
        Sanifica_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prodotti_comboBox = QtWidgets.QComboBox(Sanifica_Window)
        self.prodotti_comboBox.setGeometry(QtCore.QRect(60, 110, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.prodotti_comboBox.setFont(font)
        self.prodotti_comboBox.setStyleSheet("QComboBox::down-arrow {\n"
"\n"
"\n"
"        image: url(:/icons/res/sanifica_icon.png);\n"
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
"border-radius:15px;\n"
"border: 5px solid rgb(0,140,255);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.prodotti_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.prodotti_comboBox.setObjectName("prodotti_comboBox")
        self.metri_cubi_spinBox = QtWidgets.QSpinBox(Sanifica_Window)
        self.metri_cubi_spinBox.setGeometry(QtCore.QRect(170, 210, 151, 61))
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
        self.sanifica_btn = QtWidgets.QPushButton(Sanifica_Window)
        self.sanifica_btn.setGeometry(QtCore.QRect(400, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sanifica_btn.setFont(font)
        self.sanifica_btn.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.sanifica_btn.setObjectName("sanifica_btn")
        self.label_5 = QtWidgets.QLabel(Sanifica_Window)
        self.label_5.setGeometry(QtCore.QRect(-20, -10, 531, 41))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Sanifica_Window)
        self.label.setGeometry(QtCore.QRect(130, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Sanifica_Window)
        self.label_2.setGeometry(QtCore.QRect(300, 60, 41, 41))
        self.label_2.setStyleSheet("image: url(:/icons/res/select.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Sanifica_Window)
        self.label_3.setGeometry(QtCore.QRect(200, 160, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.cancel_btn_1 = QtWidgets.QPushButton(Sanifica_Window)
        self.cancel_btn_1.setGeometry(QtCore.QRect(0, 0, 71, 31))
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
        self.cancel_btn_ = QtWidgets.QPushButton(Sanifica_Window)
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
        self.cancel_btn_.setIcon(icon)
        self.cancel_btn_.setObjectName("cancel_btn_")

        self.retranslateUi(Sanifica_Window)
        self.cancel_btn_.clicked.connect(Sanifica_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Sanifica_Window)

    def retranslateUi(self, Sanifica_Window):
        _translate = QtCore.QCoreApplication.translate
        Sanifica_Window.setWindowTitle(_translate("Sanifica_Window", "Sanifica"))
        self.sanifica_btn.setText(_translate("Sanifica_Window", "Sanifica"))
        self.label.setText(_translate("Sanifica_Window", "Seleziona Prodotto"))
        self.label_3.setText(_translate("Sanifica_Window", "Metri Cubi"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sanifica_Window = QtWidgets.QWidget()
    ui = Ui_Sanifica_Window()
    ui.setupUi(Sanifica_Window)
    Sanifica_Window.show()
    sys.exit(app.exec_())
