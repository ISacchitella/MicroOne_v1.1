# Creazione della classe Dispositivo
# manca versione software
from datetime import timedelta

import platform

from model.ambiente_prodotto import Prodotto

IS_RASPBERRY = platform.system() == 'Linux'
class Dispositivo:

    VALORE_STANDARD_FABBRICA=28

    def __init__(self, serial_number: str):
        self.serial_number = serial_number
        self.tempo_sanificazione = None
        self.pin_sanificazione = 26

    def calcola_tempo(self, metri_cubi, concentrazione=Prodotto.CONCENTRAZIONE_STANDARD):
        self.tempo_sanificazione = timedelta(seconds=int(((metri_cubi * concentrazione)/Dispositivo.VALORE_STANDARD_FABBRICA)*60))

    def sanifica(self):
        print("Start Sanificazione")
        if not IS_RASPBERRY:
            return
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_sanificazione, GPIO.OUT)
        GPIO.output(self.pin_sanificazione, HIGH)

    def arresta(self):
        print("Stop Sanificazione")
        if not IS_RASPBERRY:
            return
        import RPi.GPIO as GPIO
        GPIO.output(self.pin_sanificazione, LOW)
        GPIO.cleanup()
