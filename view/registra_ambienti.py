# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registra_ambienti.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reg_ambiente_Window(object):
    def setupUi(self, Reg_ambiente_Window):
        Reg_ambiente_Window.setObjectName("Reg_ambiente_Window")
        Reg_ambiente_Window.resize(480, 315)
        Reg_ambiente_Window.setAutoFillBackground(False)
        Reg_ambiente_Window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome_label = QtWidgets.QLabel(Reg_ambiente_Window)
        self.nome_label.setGeometry(QtCore.QRect(17, 40, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nome_label.setFont(font)
        self.nome_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"                \n"
"image: url(:/an_ambiente/res/Anagrafica ambientale.png);\n"
"      border: 5px solid rgb(0, 134, 255);\n"
"border-radius:30px;\n"
"     ")
        self.nome_label.setText("")
        self.nome_label.setObjectName("nome_label")
        self.metri_cubi_label = QtWidgets.QLabel(Reg_ambiente_Window)
        self.metri_cubi_label.setGeometry(QtCore.QRect(330, 110, 131, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.metri_cubi_label.setFont(font)
        self.metri_cubi_label.setStyleSheet("color: rgb(0, 134, 255);")
        self.metri_cubi_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.metri_cubi_label.setObjectName("metri_cubi_label")
        self.save_btn = QtWidgets.QPushButton(Reg_ambiente_Window)
        self.save_btn.setEnabled(False)
        self.save_btn.setGeometry(QtCore.QRect(340, 240, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton:pressed{background-color: rgb(10, 57, 126);}\n"
"\n"
"QPushButton{\n"
"\n"
"background-color: rgb(0, 134, 255);\n"
"                    color: rgb(255, 255, 255);\n"
"                    border-radius:10px;\n"
"                }")
        self.save_btn.setObjectName("save_btn")
        self.metri_cubi_spinBox = QtWidgets.QSpinBox(Reg_ambiente_Window)
        self.metri_cubi_spinBox.setEnabled(False)
        self.metri_cubi_spinBox.setGeometry(QtCore.QRect(161, 110, 158, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.metri_cubi_spinBox.setFont(font)
        self.metri_cubi_spinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.metri_cubi_spinBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.metri_cubi_spinBox.setStyleSheet("QSpinBox::down-button {\n"
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
"border: 5px solid rgb(0, 134, 255);\n"
"                    border-radius:30px;\n"
"\n"
"\n"
"                    }\n"
"                ")
        self.metri_cubi_spinBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.metri_cubi_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.metri_cubi_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.metri_cubi_spinBox.setMinimum(1)
        self.metri_cubi_spinBox.setMaximum(3000)
        self.metri_cubi_spinBox.setSingleStep(1)
        self.metri_cubi_spinBox.setProperty("value", 1)
        self.metri_cubi_spinBox.setObjectName("metri_cubi_spinBox")
        self.nome_textbox = QtWidgets.QLineEdit(Reg_ambiente_Window)
        self.nome_textbox.setGeometry(QtCore.QRect(87, 40, 376, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.nome_textbox.setFont(font)
        self.nome_textbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nome_textbox.setStyleSheet("border-radius:30px;\n"
"                    background-color: rgb(0, 0, 0);\n"
"                    background-color: rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 0, 0);\n"
"                ")
        self.nome_textbox.setText("")
        self.nome_textbox.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_textbox.setObjectName("nome_textbox")
        self.label_5 = QtWidgets.QLabel(Reg_ambiente_Window)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.label_5.setStyleSheet("background-color: rgb(0, 140, 255);\n"
"image: url(:/sfondo_registra_ambiente/res/pagina_MICROONE_ins_nome_amb.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.cancel_btn_ = QtWidgets.QPushButton(Reg_ambiente_Window)
        self.cancel_btn_.setGeometry(QtCore.QRect(410, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cancel_btn_.setFont(font)
        self.cancel_btn_.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 134, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"                 color: rgb(255, 255, 255);\n"
"             \n"
"background-color: rgb(0, 134, 255);\n"
"}\n"
"QPushButton:pressed{background-color: rgb(10, 57, 126);}")
        self.cancel_btn_.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cancel/res/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn_.setIcon(icon)
        self.cancel_btn_.setFlat(True)
        self.cancel_btn_.setObjectName("cancel_btn_")
        self.keyboard_btn = QtWidgets.QPushButton(Reg_ambiente_Window)
        self.keyboard_btn.setGeometry(QtCore.QRect(10, 235, 120, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keyboard_btn.setFont(font)
        self.keyboard_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"image: url(:/keyboard/res/keyboard.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{background-color: rgb(10, 57, 126);}")
        self.keyboard_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/keyboard/res/keyboard_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.keyboard_btn.setIcon(icon1)
        self.keyboard_btn.setObjectName("keyboard_btn")
        self.concentrazione_label_2 = QtWidgets.QLabel(Reg_ambiente_Window)
        self.concentrazione_label_2.setGeometry(QtCore.QRect(354, 110, 31, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concentrazione_label_2.sizePolicy().hasHeightForWidth())
        self.concentrazione_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.concentrazione_label_2.setFont(font)
        self.concentrazione_label_2.setStyleSheet("color: rgb(0, 134, 255);")
        self.concentrazione_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.concentrazione_label_2.setObjectName("concentrazione_label_2")
        self.label_5.raise_()
        self.nome_label.raise_()
        self.metri_cubi_label.raise_()
        self.save_btn.raise_()
        self.metri_cubi_spinBox.raise_()
        self.nome_textbox.raise_()
        self.cancel_btn_.raise_()
        self.keyboard_btn.raise_()
        self.concentrazione_label_2.raise_()

        self.retranslateUi(Reg_ambiente_Window)
        self.cancel_btn_.clicked.connect(Reg_ambiente_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Reg_ambiente_Window)

    def retranslateUi(self, Reg_ambiente_Window):
        _translate = QtCore.QCoreApplication.translate
        Reg_ambiente_Window.setWindowTitle(_translate("Reg_ambiente_Window", "Registra Ambiente"))
        self.metri_cubi_label.setText(_translate("Reg_ambiente_Window", "m"))
        self.save_btn.setText(_translate("Reg_ambiente_Window", "Salva"))
        self.concentrazione_label_2.setText(_translate("Reg_ambiente_Window", "3"))
import img_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reg_ambiente_Window = QtWidgets.QWidget()
    ui = Ui_Reg_ambiente_Window()
    ui.setupUi(Reg_ambiente_Window)
    Reg_ambiente_Window.show()
    sys.exit(app.exec_())
