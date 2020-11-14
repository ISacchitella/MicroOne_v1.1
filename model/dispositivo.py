# Creazione della classe Dispositivo
# manca versione software
import sys
from datetime import timedelta

from model.ambiente_prodotto import Prodotto

IS_RASPBERRY = sys.platform.startswith('linux')

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
        GPIO.output(self.pin_sanificazione, GPIO.HIGH)

    def arresta(self):
        print("Stop Sanificazione")
        if not IS_RASPBERRY:
            return
        import RPi.GPIO as GPIO
        GPIO.output(self.pin_sanificazione, GPIO.LOW)
        GPIO.cleanup()

    def set_system_time(self, inserted_time):
        print('Setting time')
        if not IS_RASPBERRY:
            return 1
        try:
            import ctypes
            import ctypes.util
            import time
            # /usr/include/linux/time.h:
            #
            # define CLOCK_REALTIME                     0
            CLOCK_REALTIME = 0

            # /usr/include/time.h
            #
            # struct timespec
            #  {
            #    __time_t tv_sec;            /* Seconds.  */
            #    long int tv_nsec;           /* Nanoseconds.  */
            #  };
            class timespec(ctypes.Structure):
                _fields_ = [("tv_sec", ctypes.c_long),
                            ("tv_nsec", ctypes.c_long)]

            librt = ctypes.CDLL(ctypes.util.find_library("rt"))

            ts = timespec()
            ts.tv_sec = int(time.mktime(inserted_time.timetuple()))
            ts.tv_nsec = inserted_time.microsecond * 1000  # Microsecond to nanosecond

            # http://linux.die.net/man/3/clock_settime
            librt.clock_settime(CLOCK_REALTIME, ctypes.byref(ts))
            print('No error in time setting')
            return 0
        except Exception as ex:
            template: str = "Impossibile modificare l'orario di sistema: type {0}. Arguments:\n{1!r}"
            message: str = template.format(type(ex).__name__, ex.args)
            print(template + ex,file=sys.stderr)
            return -1
