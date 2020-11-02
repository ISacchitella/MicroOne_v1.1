import logging
from collections import OrderedDict
from datetime import timedelta, datetime
from enum import Enum, auto
from time import sleep

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

from control.save import load_ambienti, save_ambienti, load_prodotti, save_prodotti, save_info, get_system_info, \
    copy_info
from model.ambiente_prodotto import Ambiente, check_metri_cubi, Prodotto, TEMPO_ALLONTANAMENTO
from view.timer_window import Ui_Timer_Window

LOGGER_NAME = 'root'
ONE_SECOND = timedelta(seconds=1)


def make_logger():
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    file_handler = logging.FileHandler('errors.log', mode='w')
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
    logger = logging.getLogger(LOGGER_NAME)
    try:
        prodotti = load_prodotti()
        nome = ui.nome_textbox.text()
        data = ui.data_scad_dateEdit.date().toPyDate()
        if nome != None and nome != '':
            prodotti.append(Prodotto(nome, data))
            save_prodotti(prodotti)
            window.close()
        else:
            print('Scrivi il nome')
    except Exception as ex:
        logger.exception(make_error_msg(ex))


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
        print('Scrivi il nome')


def seleziona_ambiente(window, ui, app):
    app.selected_ambiente = ui.comboBox.currentText().split(':')[0]
    window.close()


def seleziona_prodotto(ui, app, prodotti):
    app.selected_prodotto = next(
        (prodotto for prodotto in prodotti if prodotto.nome == ui.prodotti_comboBox.currentText()))


class Stato(Enum):
    FALLITA = 0
    COMPLETATA = 1


# Sanifica Widgets Controller
def sanifica(window, ui, app):
    logger = logging.getLogger(LOGGER_NAME)
    try:
        timer_window = QtWidgets.QWidget()
        timer_ui = Ui_Timer_Window()
        timer_ui.setupUi(timer_window)
        timer_ui.allontanarsi_sec = TEMPO_ALLONTANAMENTO
        timer_ui.tempo_sanificazione = app.dispositivo.calcola_tempo(ui.metri_cubi_spinBox.value(),
                                                                     concentrazione=app.selected_prodotto.get_concentrazione())
        sessione = OrderedDict({
            'data': datetime.now().strftime("%H:%M:%S %d/%m/%y"),
            'tempo': str(timer_ui.tempo_sanificazione),
            'stato': Stato.FALLITA.name,
            'ambiente': app.selected_ambiente,
            'metri_cubi': ui.metri_cubi_spinBox.value(),
            'prodotto': app.selected_prodotto.__dict__()
        })
        app.info['anagrafica'].insert(0, sessione)
        app.info['sistema'] = get_system_info()
        save_info(app.info)
        timer_ui.timer = QtCore.QTimer()
        timer_ui.timer.timeout.connect(lambda: timeout_allontanarsi(timer_window, timer_ui, app))
        timer_ui.timer.start(1000)
        timer_ui.timer.startTimer(timer_ui.allontanarsi_sec, timerType=Qt.VeryCoarseTimer)
        timer_window.show()
        window.close()
    except Exception as ex:
        logger.exception(make_error_msg(ex))


def timeout_allontanarsi(window, ui, app):
    logger = logging.getLogger(LOGGER_NAME)
    try:
        ui.allontanarsi_sec -= 1
        ui.timer_label.setText(str(ui.allontanarsi_sec))
        if ui.allontanarsi_sec <= 0:
            ui.timer.stop()
            ui.timer.disconnect()
            ui.description_label.setText("Sanificazione in corso!")
            ui.timer_label.setText(str(ui.tempo_sanificazione))
            ui.timer.timeout.connect(lambda: timeout_sanificazione(window, ui, app))
            ui.timer.start(1000)
            ui.timer.startTimer(ui.tempo_sanificazione.total_seconds(), timerType=Qt.VeryCoarseTimer)
    except Exception as ex:
        logger.exception(make_error_msg(ex))


def timeout_sanificazione(window, ui, app):
    logger = logging.getLogger(LOGGER_NAME)
    try:
        ui.tempo_sanificazione -= ONE_SECOND
        ui.timer_label.setText(str(ui.tempo_sanificazione))
        if ui.tempo_sanificazione.total_seconds() <= 0:
            ui.timer.stop()
            ui.description_label.setText("Trattamento completato!")
            app.info['anagrafica'][0]['stato'] = Stato.COMPLETATA.name
            save_info(app.info)
            ui.cancel_btn.setEnabled(True)
            ui.download_btn.setEnabled(True)
            ui.download_btn.clicked.connect(lambda: copy_info(app.info['sistema']['disk']['disk_partitions']))
    except Exception as ex:
        logger.exception(make_error_msg(ex))
        window.close()
