from datetime import date, datetime

from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel
from PyQt5 import QtCore
from control.controllers import salva_prodotto, salva_ambiente, make_logger, make_error_msg, \
    open_seleziona_prodotto
from control.keyboard_controller import Keyboard
from control.save import load_info, save_info, format_info, copy_info, get_system_info, \
    poweroff
from model.ambiente_prodotto import MAX_METRI_CUBI
from model.dispositivo import Dispositivo
# https://stackoverflow.com/questions/7031962/qdateedit-calendar-popup
from view.inserisci_data_di_oggi_window import Ui_Inserisci_Data_di_Oggi_Window
from view.main_window import Ui_MainWindow, QtWidgets
from view.recap_info_window import Ui_recap_info_window
from view.registra_ambienti import Ui_Reg_ambiente_Window
from view.registra_prodotti import Ui_Reg_prodotto_Window


class Micro_One_App(Ui_MainWindow):
    '''Application Entry Point'''

    def __init__(self, window):
        self.info = load_info()
        super(Ui_MainWindow, self).__init__()
        self.setupUi(window)
        self.initUI()
        self.window = window
        self.window.show()

    # ---------Metodi------------------------------------------

    def initUI(self):
        '''Gestione eventi della Pagina MainWindow (Menù principale)+Settaggio del Serial Number'''
        self.sanifica_btn.clicked.connect(self.open_sanifica_window)
        self.reg_prodotto_btn.clicked.connect(self.open_reg_prodotto_window)
        self.reg_ambiente_btn.clicked.connect(self.open_reg_ambiente_window)
        self.settings_btn.clicked.connect(self.open_recap_info_window)
        self.poweroff_btn.clicked.connect(poweroff)
        self.selected_ambiente = None
        self.selected_prodotto = None
        self.selected_metri_cubi = 1
        self.current_date = datetime.now()
        # Verifica la presenza del dispositivo
        has_serial_number = not (
                self.info == None or len(self.info) == 0 or 'serial_number' not in self.info or self.info[
            'serial_number'] in [None, ''])
        if has_serial_number:
            self.dispositivo = Dispositivo(self.info['serial_number'])
        else:
            self.dispositivo = None
            self.setup_serial_number()
            self.info['serial_number'] = self.dispositivo.serial_number
            save_info(self.info)
        self.serial_label.setText("MicroOne-" + self.dispositivo.serial_number)
        if 'versione' not in self.info.keys():
            self.info['versione'] = "v1.1"
        if 'anagrafica' not in self.info.keys():
            self.info['anagrafica'] = []

    def setup_serial_number(self):
        serial_number_dialog = QDialog()
        serial_number_dialog.setModal(True)  # impedisce alla finestra principale di interferire
        serial_number_dialog.setObjectName("serial_number_dialog")
        serial_number_dialog.setStyleSheet("background-color: rgb(255,255,255); \n")
        serial_number_dialog.resize(240, 140)
        serial_number_dialog.setWindowTitle("Serial Number")

        sn_textbox = QLineEdit(serial_number_dialog)
        sn_textbox.move(10, 30)
        sn_textbox.resize(220, 40)
        sn_textbox.setStyleSheet("color: rgb(0,0,0); \n"
                                 "border-radius: 10px; \n"
                                 "border: 5px solid rgb(0,140,255); \n")
        # button
        sn_button = QPushButton('Salva', serial_number_dialog)
        sn_button.move(150, 80)
        sn_button.resize(75, 34)
        sn_button.setStyleSheet("background-color: rgb(0, 140, 255); \n"
                                "color: rgb(0,0,0); \n"
                                "border-radius: 10px; \n"
                                "border: 5px solid rgb(0,140,255); \n")

        sn_label = QLabel("Inserisci seriale dispositivo", serial_number_dialog)
        sn_label.setBuddy(sn_textbox)
        sn_label.setStyleSheet("color: rgb(0,0,0); \n"
                               "font-size: 15px; \n")


        sn_button.clicked.connect(lambda: self.salva_seriale(serial_number_dialog, sn_textbox))
        serial_number_dialog.exec()

    # ------------Bindings---------------------

    def salva_seriale(self, serial_number_dialog, sn_textbox):
        self.dispositivo = Dispositivo(sn_textbox.text())
        serial_number_dialog.close()

    def open_recap_info_window(self):
        self.recap_info_window = QtWidgets.QWidget()
        self.recap_info_ui = Ui_recap_info_window()
        self.recap_info_ui.setupUi(self.recap_info_window)
        self.recap_info_ui.recap_info_text_edit.setText(format_info(self.info))
        self.info['sistema'] = get_system_info()
        self.recap_info_ui.download_btn.clicked.connect(copy_info)
        save_info(self.info)
        self.recap_info_window.show()


    def open_sanifica_window(self):
        self.data_oggi_window = QtWidgets.QWidget()
        self.data_oggi_ui = Ui_Inserisci_Data_di_Oggi_Window()
        self.data_oggi_ui.setupUi(self.data_oggi_window)
        QDate_temp = QtCore.QDate.currentDate()
        QTime_temp = QtCore.QTime.currentTime()
        self.current_date = datetime.combine(QDate_temp.toPyDate(), QTime_temp.toPyTime())
        self.data_oggi_ui.data_oggi_dateTimeEdit.setDateTime(QtCore.QDateTime(QDate_temp, QTime_temp))#TODO
        self.sanifica_index = 0
        self.data_oggi_ui.avanti_btn.clicked.connect(lambda: open_seleziona_prodotto(self.data_oggi_window, self.data_oggi_ui, self))
        self.data_oggi_window.show()

    def open_reg_prodotto_window(self):
        self.reg_prodotto_window = QtWidgets.QWidget()
        self.reg_prodotto_ui = Ui_Reg_prodotto_Window()
        self.reg_prodotto_ui.setupUi(self.reg_prodotto_window)
        self.reg_prodotto_ui.save_btn.clicked.connect(
            lambda: salva_prodotto(self.reg_prodotto_window, self.reg_prodotto_ui))
        self.reg_prodotto_ui.keyboard_btn.clicked.connect(Keyboard.open_keyboard)
        self.reg_prodotto_window.show()

    def open_reg_ambiente_window(self):
        self.reg_ambiente_window = QtWidgets.QWidget()
        self.reg_ambiente_ui = Ui_Reg_ambiente_Window()
        self.reg_ambiente_ui.setupUi(self.reg_ambiente_window)
        self.reg_ambiente_ui.metri_cubi_spinBox.setMaximum(MAX_METRI_CUBI)
        self.reg_ambiente_ui.save_btn.clicked.connect(
            lambda: salva_ambiente(self.reg_ambiente_window, self.reg_ambiente_ui))
        self.reg_ambiente_ui.keyboard_btn.clicked.connect(Keyboard.open_keyboard)
        self.reg_ambiente_window.show()

    # def open_sel_ambiente_window(self):
    #     self.sel_ambiente_window = QtWidgets.QWidget()
    #     self.sel_ambiente_ui = Ui_Sel_ambiente_Window()
    #     self.sel_ambiente_ui.setupUi(self.sel_ambiente_window)
    #     self.sel_ambiente_ui.comboBox.clear()
    #     ambienti = load_ambienti()
    #     for ambiente in ambienti:
    #         self.sel_ambiente_ui.comboBox.addItem(display_ambiente(ambiente))
    #     self.sel_ambiente_ui.comboBox.currentTextChanged.connect(
    #         lambda: seleziona_ambiente(self.sel_ambiente_window, self.sel_ambiente_ui, self))
    #     self.sel_ambiente_window.show()


if __name__ == "__main__":
    import sys
    try:
        logger = make_logger()
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        ui = Micro_One_App(window)
        sys.exit(app.exec_())
    except Exception as ex:
        logger.exception(make_error_msg(ex))
