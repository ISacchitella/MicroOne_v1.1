from model.dispositivo import IS_RASPBERRY
from os import system

class Keyboard():
    OPEN_COMMAND = "matchbox-keyboard"
    @classmethod
    def open_keyboard(cls):
        print("keyboard OPENED")
        if not IS_RASPBERRY:
            return
        system(Keyboard.OPEN_COMMAND)

    # @classmethod
    # def close_keyboard(cls):
    #     print("keyboard CLOSED")