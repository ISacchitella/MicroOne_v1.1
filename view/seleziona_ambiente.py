# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seleziona_ambiente.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sel_ambiente_Window(object):
    def setupUi(self, Sel_ambiente_Window):
        Sel_ambiente_Window.setObjectName("Sel_ambiente_Window")
        Sel_ambiente_Window.resize(480, 320)
        Sel_ambiente_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox = QtWidgets.QComboBox(Sel_ambiente_Window)
        self.comboBox.setGeometry(QtCore.QRect(87, 40, 376, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox::down-arrow {\n"
"\n"
"\n"
"        image: url(:/arrows/res/down_arrow.png);\n"
"        width: 14px;\n"
"        height: 14px;\n"
"\n"
"        }\n"
"        QComboBox::drop-down\n"
"        {\n"
"        border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"\n"
"        }\n"
"\n"
"QComboBox {\n"
"    color: black;\n"
"border-radius:30px;\n"
"border: 5px solid rgb(0,140,255);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.comboBox.setMaxVisibleItems(100)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(Sel_ambiente_Window)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"image: url(:/sfondo_microone/res/pagina_MICROONE.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Sel_ambiente_Window)
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
        self.nome_label = QtWidgets.QLabel(Sel_ambiente_Window)
        self.nome_label.setGeometry(QtCore.QRect(17, 40, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(:/hand/res/Hand.png);\n"
"      border: 5px solid rgb(0,140,255);\n"
"border-radius:30px;\n"
"     ")
        self.nome_label.setText("")
        self.nome_label.setObjectName("nome_label")
        self.cancel_btn_ = QtWidgets.QPushButton(Sel_ambiente_Window)
        self.cancel_btn_.setGeometry(QtCore.QRect(410, 0, 51, 31))
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
        self.cancel_btn_.setFlat(True)
        self.cancel_btn_.setObjectName("cancel_btn_")
        self.avanti_btn = QtWidgets.QPushButton(Sel_ambiente_Window)
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
        self.label_5.raise_()
        self.comboBox.raise_()
        self.nome_label.raise_()
        self.cancel_btn_.raise_()
        self.avanti_btn.raise_()
        self.label.raise_()

        self.retranslateUi(Sel_ambiente_Window)
        self.cancel_btn_.clicked.connect(Sel_ambiente_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Sel_ambiente_Window)

    def retranslateUi(self, Sel_ambiente_Window):
        _translate = QtCore.QCoreApplication.translate
        Sel_ambiente_Window.setWindowTitle(_translate("Sel_ambiente_Window", "Seleziona Ambiente"))
        self.label.setText(_translate("Sel_ambiente_Window", "Seleziona Ambiente"))
        self.avanti_btn.setText(_translate("Sel_ambiente_Window", "Avanti"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sel_ambiente_Window = QtWidgets.QWidget()
    ui = Ui_Sel_ambiente_Window()
    ui.setupUi(Sel_ambiente_Window)
    Sel_ambiente_Window.show()
    sys.exit(app.exec_())
