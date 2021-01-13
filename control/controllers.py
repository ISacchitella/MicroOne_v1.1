import logging
from collections import OrderedDict
from datetime import timedelta
from enum import Enum
from time import sleep

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

from control.keyboard_controller import Keyboard
from control.literals import DATA, TEMPO, STATO, AMBIENTE, METRI_CUBI, PRODOTTO, ANAGRAFICA
from control.save import load_ambienti, save_ambienti, load_prodotti, save_prodotti, save_info, get_system_info, \
    display_riepilogo, close_timer
from model.ambiente_prodotto import Ambiente, check_metri_cubi, Prodotto, TEMPO_ALLONTANAMENTO, display_ambiente, \
    MAX_METRI_CUBI
from view.inserisci_data_scadenza_window import Ui_Inserisci_Data_Scadenza_Window
from view.inserisci_lotto_window import Ui_Inserisci_Lotto_Window
from view.inserisci_metri_cubi_window import Ui_Inserisci_Metri_Cubi_Window
from view.recap_info_sanifica_window import Ui_recap_info_sanifica_window
from view.seleziona_ambiente import Ui_Sel_ambiente_Window
from view.seleziona_prodotto_window import Ui_Seleziona_Prodotto_Window
from view.timer_window import Ui_Timer_Window

LOGGER_NAME = 'root'
ONE_SECOND = timedelta(seconds=1)


def make_logger():
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    file_handler = logging.FileHandler('../errors.log', mode='w')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter(
        '%(levelname)s-%(asctime)s\nmessagge: %(message)s\nmodule: %(module)s\nfunction: %(funcName)s\nline: %(lineno)d\n'))
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def make_error_msg(ex):
    template: str = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message: str = template.format(type(ex).__name__, ex.args)
    return message


# ----------------Bindings-------------------
# Prodotto Widgets Controller
def salva_prodotto(window, ui):
    prodotti = load_prodotti()
    nome = ui.nome_textbox.text()
    # data = ui.data_scad_dateEdit.date().toPyDate()
    concentrazione = ui.concentrazione_spinBox.value()
    if nome != None and nome != '':
        prodotti.append(Prodotto(nome, concentrazione))
        save_prodotti(prodotti)
        window.close()
    else:
        print('Write the name')


# Ambiente Widgets Controller
def salva_ambiente(window, ui):
    ambienti = load_ambienti()
    nome = ui.nome_textbox.text()
    metri_cubi = ui.metri_cubi_spinBox.value()
    if nome != None and nome != '':
        ambienti.append(Ambiente(nome, check_metri_cubi(metri_cubi)))
        save_ambienti(ambienti)
        window.close()
    else:
        print('Write the name')


def seleziona_ambiente(ui, app):
    if ui.comboBox.currentText() != "":
        app.selected_ambiente = ui.comboBox.currentText().split(':')[0]


def seleziona_prodotto(ui, app, prodotti):
    if ui.prodotti_comboBox.currentText() == "":
        app.selected_prodotto = None
        ui.avanti_btn.setDisabled(True)
    else:
        app.selected_prodotto = next(
            (prodotto for prodotto in prodotti if prodotto.nome == ui.prodotti_comboBox.currentText().split(':')[0]))
        ui.avanti_btn.setEnabled(True)


def make_window(ui_class):
    next_window = QtWidgets.QWidget(flags=(Qt.Widget | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
    next_ui = ui_class()
    next_ui.setupUi(next_window)
    return [next_window, next_ui]


def move_to_next_window(app, current_window, current_ui, next_window, next_ui, focus=None):
    app.sanifica_index += 1
    if app.sanifica_index >= len(WINDOWS_LIST):
        app.sanifica_index = 0
        next_ui.avanti_btn.clicked.connect(lambda: sanifica(next_window, next_ui, app))
    else:
        next_ui.avanti_btn.clicked.connect(lambda: WINDOWS_LIST[app.sanifica_index][0](next_window, next_ui, app))
    current_window.close()
    if hasattr(next_ui, 'keyboard_btn'):
        next_ui.keyboard_btn.clicked.connect(lambda: Keyboard.open_keyboard(focus))
    next_window.show()


# ------sanifica bindings-------
def open_seleziona_prodotto(current_window, current_ui, app):
    # ----Init----
    temp = make_window(WINDOWS_LIST[app.sanifica_index][1])
    next_window = temp[0]
    next_ui = temp[1]
    # -----Middle-----
    app.current_date = current_ui.data_oggi_dateTimeEdit.dateTime().toPyDateTime()
    app.dispositivo.set_system_time(app.current_date)  # TODO
    prodotti = load_prodotti()
    prodotti_str_list = [str(prodotto) for prodotto in prodotti if
                         prodotto.data_scadenza == None or prodotto.data_scadenza > app.current_date.date() or prodotto.data_scadenza < app.current_date.date()]
    prodotti_str_list.insert(0, "")
    next_ui.prodotti_comboBox.clear()
    next_ui.prodotti_comboBox.addItems(prodotti_str_list)
    if len(prodotti_str_list) <= 1 or next_ui.prodotti_comboBox.currentText() == "":
        app.selected_prodotto = None
        next_ui.avanti_btn.setDisabled(True)
    else:
        app.selected_prodotto = next((prodotto for prodotto in prodotti if
                                      prodotto.nome ==
                                      next_ui.prodotti_comboBox.currentText().split(':')[0]))
        next_ui.avanti_btn.setEnabled(True)
    next_ui.prodotti_comboBox.currentTextChanged.connect(
        lambda: seleziona_prodotto(next_ui, app, prodotti))
    # -----End-------
    move_to_next_window(app, current_window, current_ui, next_window, next_ui)


def open_lotto(current_window, current_ui, app):
    # ----Init----
    temp = make_window(WINDOWS_LIST[app.sanifica_index][1])
    next_window = temp[0]
    next_ui = temp[1]
    # -----Middle-----
    if app.selected_prodotto.lotto != None and len(app.selected_prodotto.lotto) != 0:
        next_ui.lotto_textbox.setText(app.selected_prodotto.lotto[0])
    else:
        next_ui.lotto_textbox.setText("---")

    # -----End-------
    move_to_next_window(app, current_window, current_ui, next_window, next_ui, focus=next_ui.lotto_textbox.setFocus)


def open_data_scadenza(current_window, current_ui, app):
    # ----Init----
    temp = make_window(WINDOWS_LIST[app.sanifica_index][1])
    next_window = temp[0]
    next_ui = temp[1]
    # -----Middle-----
    new_lotto = current_ui.lotto_textbox.text()
    if new_lotto != '' and new_lotto not in app.selected_prodotto.lotto:
        app.selected_prodotto.lotto.insert(0, new_lotto)
    if app.selected_prodotto.data_scadenza != None:
        scadenza = app.selected_prodotto.data_scadenza
        next_ui.data_scad_dateEdit.setDate(QtCore.QDate(scadenza.year, scadenza.month, scadenza.day))
    # -----End-------
    move_to_next_window(app, current_window, current_ui, next_window, next_ui,
                        focus=next_ui.data_scad_dateEdit.setFocus)


def open_ambiente(current_window, current_ui, app):
    # ----Init----
    temp = make_window(WINDOWS_LIST[app.sanifica_index][1])
    next_window = temp[0]
    next_ui = temp[1]
    # -----Middle-----
    app.selected_prodotto.data_scadenza = current_ui.data_scad_dateEdit.date().toPyDate()
    prodotti = load_prodotti()
    prodotto_old_version = [prodotto for prodotto in prodotti if prodotto.nome == app.selected_prodotto.nome]
    if len(prodotto_old_version) > 0 and prodotto_old_version[0] != None:
        prodotti.remove(prodotto_old_version[0])
        prodotti.append(app.selected_prodotto)
        save_prodotti(prodotti)
    next_ui.comboBox.clear()
    ambienti = load_ambienti()
    next_ui.comboBox.addItem("")
    for ambiente in ambienti:
        next_ui.comboBox.addItem(display_ambiente(ambiente))
    next_ui.comboBox.currentTextChanged.connect(
        lambda: seleziona_ambiente(next_ui, app))
    # -----End-------
    move_to_next_window(app, current_window, current_ui, next_window, next_ui)


def open_metri_cubi(current_window, current_ui, app):
    # ----Init----
    temp = make_window(WINDOWS_LIST[app.sanifica_index][1])
    next_window = temp[0]
    next_ui = temp[1]
    # -----Middle-----
    ambienti = load_ambienti()
    next_ui.metri_cubi_spinBox.setMaximum(MAX_METRI_CUBI)
    if app.selected_ambiente != None:
        ambiente_selezionato = next((ambiente for ambiente in ambienti if ambiente.name == app.selected_ambiente))
        app.selected_metri_cubi = ambiente_selezionato.cubic_meters
    next_ui.metri_cubi_spinBox.setValue(app.selected_metri_cubi)

    # -----End-------
    move_to_next_window(app, current_window, current_ui, next_window, next_ui,
                        focus=next_ui.metri_cubi_spinBox.setFocus)


def open_riepilogo(current_window, current_ui, app):
    # ----Init----
    temp = make_window(WINDOWS_LIST[app.sanifica_index][1])
    next_window = temp[0]
    next_ui = temp[1]
    # -----Middle-----
    app.selected_metri_cubi = current_ui.metri_cubi_spinBox.value()
    app.selected_prodotto.millilitri = app.selected_metri_cubi
    if app.selected_prodotto.millilitri <= Prodotto.MAX_MILLILITRI:
        next_ui.millilitri_label.setText(
            "Needed " + str(app.selected_prodotto.millilitri) + " ml of product. \n"
                                                                        "Check the tank!")

    else:
        next_ui.millilitri_label.setText("It is not possible to" + "\n" + "run medical procedure!")
        next_ui.avanti_btn.setDisabled(True)

    app.dispositivo.calcola_tempo(app.selected_metri_cubi, concentrazione=app.selected_prodotto.get_concentrazione())

    sessione = OrderedDict({
        DATA: app.current_date.strftime("%H:%M:%S %d/%m/%y"),
        TEMPO: str(app.dispositivo.tempo_sanificazione),
        STATO: Stato.FAILED.name,
        AMBIENTE: app.selected_ambiente,
        METRI_CUBI: app.selected_metri_cubi,
        PRODOTTO: app.selected_prodotto.__dict__()
    })
    app.info[ANAGRAFICA].insert(0, sessione)
    next_ui.recap_info_text_edit.setText(display_riepilogo(sessione))
    # -----End-------
    move_to_next_window(app, current_window, current_ui, next_window, next_ui)


WINDOWS_LIST = [(open_seleziona_prodotto, Ui_Seleziona_Prodotto_Window), (open_lotto, Ui_Inserisci_Lotto_Window),
                (open_data_scadenza, Ui_Inserisci_Data_Scadenza_Window),
                (open_ambiente, Ui_Sel_ambiente_Window), (open_metri_cubi, Ui_Inserisci_Metri_Cubi_Window),
                (open_riepilogo, Ui_recap_info_sanifica_window)]


# ---------timer-------
class Stato(Enum):
    FAILED = 0
    COMPLETED = 1


def sanifica(window, ui, app):
    timer_window = QtWidgets.QWidget(flags=(Qt.Widget | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
    timer_ui = Ui_Timer_Window()
    timer_ui.setupUi(timer_window)
    timer_ui.close_btn.clicked.connect(lambda: close_timer(timer_window, timer_ui.timer.stop))
    timer_ui.allontanarsi_sec = TEMPO_ALLONTANAMENTO
    timer_ui.tempo_sanificazione = app.dispositivo.tempo_sanificazione
    app.info['sistema'] = get_system_info()
    save_info(app.info)
    timer_ui.timer = QtCore.QTimer()
    timer_ui.timer.timeout.connect(lambda: timeout_allontanarsi(timer_window, timer_ui, app))
    timer_ui.timer.start(1000)
    timer_ui.timer.startTimer(timer_ui.allontanarsi_sec, timerType=Qt.VeryCoarseTimer)
    timer_window.show()
    window.close()


def timeout_allontanarsi(window, ui, app):
    ui.allontanarsi_sec -= 1
    ui.timer_label.setText(str(ui.allontanarsi_sec))
    if ui.allontanarsi_sec <= 0:
        ui.timer.stop()
        ui.timer.disconnect()  # TODO aumentare o diminuire scritta timer
        ui.description_label.setText("Ongoing Disinfection...")
        ui.description_label.setStyleSheet("color: rgb(85,170,0); \n"
                                           "font-size: 20px; \n")
        ui.timer_label.setText(str(ui.tempo_sanificazione))
        ui.timer_label.setStyleSheet("color: rgb(85,170,0);")
        ui.close_btn.clicked.connect(lambda: close_timer(window, ui.timer.stop, arresta=app.dispositivo.arresta))
        ui.timer.timeout.connect(lambda: timeout_sanificazione(window, ui, app))
        ui.timer.start(1000)
        ui.timer.startTimer(ui.tempo_sanificazione.total_seconds(), timerType=Qt.VeryCoarseTimer)
        app.dispositivo.sanifica()


def timeout_sanificazione(window, ui, app):
    ui.tempo_sanificazione -= ONE_SECOND
    ui.timer_label.setText(str(ui.tempo_sanificazione))
    if ui.tempo_sanificazione.total_seconds() <= 0:
        ui.timer_label.setText('0')
        app.dispositivo.arresta()
        ui.timer.stop()
        ui.close_btn.disconnect()
        ui.close_btn.clicked.connect(lambda: close_timer(window, ui.timer.stop, arresta=None))
        ui.description_label.setText("Treatment completed!")
        app.info[ANAGRAFICA][0][STATO] = Stato.COMPLETED.name
        save_info(app.info)
        ui.cancel_btn.setEnabled(False)
        ui.download_btn.setEnabled(True)
        ui.timer.disconnect()
        sleep(10)
        ui.description_label.setText("Ongoing Decontamination...")
        ui.description_label.setStyleSheet("color: rgb(170, 0, 0);\n"
                                           "font-size: 18px;")
        ui.decontaminazione_sec = timedelta(hours=1)
        ui.timer_label.setText(str(ui.decontaminazione_sec))
        ui.timer_label.setStyleSheet("color: rgb(170, 0, 0);")
        ui.timer.timeout.connect(lambda: timeout_decontaminazione(window, ui, app))
        ui.timer.start(1000)
        ui.timer.startTimer(ui.decontaminazione_sec.total_seconds(), timerType=Qt.VeryCoarseTimer)


def timeout_decontaminazione(window, ui, app):
    ui.decontaminazione_sec -= ONE_SECOND
    ui.timer_label.setText(str(ui.decontaminazione_sec))
    if ui.decontaminazione_sec.total_seconds() <= 0:
        ui.timer.stop()
        ui.cancel_btn.setDisabled(True)
        ui.description_label.setText("Decontamination completed!")
        ui.description_label.setStyleSheet("color: rgb(85,170,0); \n"
                                           "font-size: 20px;")
