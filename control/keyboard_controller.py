from model.dispositivo import IS_RASPBERRY
from os import system
from multiprocessing import Process


class Keyboard():
    OPEN_COMMAND = "dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show"

    @classmethod
    def open_keyboard_salva_ambienti(cls, ui):
        if ui != None:
            if ui.nome_textbox.text() == '':
                ui.nome_textbox.setFocus()
            else:
                ui.metri_cubi_spinBox.setFocus()
        keyboard = Process(target=Keyboard.exec_command, args=())
        keyboard.start()

    @classmethod
    def open_keyboard_salva_prodotti(cls, ui):
        if ui != None:
            if ui.nome_textbox.text() == '':
                ui.nome_textbox.setFocus()
            else:
                ui.concentrazione_spinBox.setFocus()
        keyboard = Process(target=Keyboard.exec_command, args=())
        keyboard.start()

    @classmethod
    def open_keyboard(cls, focus_func):
        if focus_func != None:
            focus_func()
        keyboard = Process(target=Keyboard.exec_command, args=())
        keyboard.start()

    @classmethod
    def exec_command(cls):
        print("keyboard OPENED")
        if not IS_RASPBERRY:
            return
        system(Keyboard.OPEN_COMMAND)
    # @classmethod
    # def close_keyboard(cls):
    #     print("keyboard CLOSED")
