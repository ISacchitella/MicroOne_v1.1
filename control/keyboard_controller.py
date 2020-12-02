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
                ui.metri_cubi_spinBox.setDisabled(True)
                ui.save_btn.setDisabled(True)
            else:
                ui.nome_textbox.setStyleSheet('''border-radius:30px; 
                                background-color: rgb(0, 0, 0);
                                    background-color: rgb(255, 255, 255);
                                    border: 5px solid rgb(0, 134, 255);
                                ''')
                ui.metri_cubi_spinBox.setDisabled(False)
                ui.metri_cubi_spinBox.setStyleSheet('''QSpinBox::down-button {
  image: url(:/arrows/res/down_arrow.png);
  width: 50px;
}

QSpinBox::up-button {
  image: url(:/arrows/res/up_arrow.png);
  width: 50px;
}

QSpinBox {
  color: rgb(0, 0, 0);
  background-color: rgb(255, 255, 255);
  border: 5px solid rgb(255, 0, 0);
  border-radius: 30px;
}''')
                ui.metri_cubi_spinBox.setFocus()
                ui.save_btn.setDisabled(False)
        keyboard = Process(target=Keyboard.exec_command, args=())
        keyboard.start()

    @classmethod
    def open_keyboard_salva_prodotti(cls, ui):
        if ui != None:
            if ui.nome_textbox.text() == '':
                ui.nome_textbox.setFocus()
                ui.concentrazione_spinBox.setDisabled(True)
                ui.save_btn.setDisabled(True)
            else:
                ui.nome_textbox.setStyleSheet('''border-radius:30px; 
                                                background-color: rgb(0, 0, 0);
                                                    background-color: rgb(255, 255, 255);
                                                    border: 5px solid rgb(0, 134, 255);
                                                ''')
                ui.concentrazione_spinBox.setDisabled(False)
                ui.concentrazione_spinBox.setStyleSheet('''QSpinBox::down-button {
                  image: url(:/arrows/res/down_arrow.png);
                  width: 50px;
                }

                QSpinBox::up-button {
                  image: url(:/arrows/res/up_arrow.png);
                  width: 50px;
                }

                QSpinBox {
                  color: rgb(0, 0, 0);
                  background-color: rgb(255, 255, 255);
                  border: 5px solid rgb(255, 0, 0);
                  border-radius: 30px;
                }''')
                ui.concentrazione_spinBox.setFocus()
                ui.save_btn.setDisabled(False)
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
