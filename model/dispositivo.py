# Creazione della classe Dispositivo
# manca versione software
from datetime import timedelta

from model.ambiente_prodotto import Prodotto


class Dispositivo:

    def __init__(self, serial_number: str):
        self.serial_number = serial_number

    def calcola_tempo(self, metri_cubi, concentrazione=Prodotto.CONCENTRAZIONE_STANDARD):
        return timedelta(seconds=metri_cubi * concentrazione)

    def sanifica(self, prodotto, ambiente):
        pass

    def arresta(self):
        pass
