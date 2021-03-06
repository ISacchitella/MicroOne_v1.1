from collections import namedtuple, OrderedDict
from datetime import datetime

from control.literals import NOME_AMBIENTE, METRI_CUBI, NOME_PRODOTTO, DATA_SCADENZA, CONCENTRAZIONE, LOTTO

'''Timer misurato in secondi'''
TEMPO_ALLONTANAMENTO = 10
'''Ambiente'''
Ambiente = namedtuple('Ambiente', [NOME_AMBIENTE, METRI_CUBI])
MAX_METRI_CUBI = 3000
MIN_METRI_CUBI = 1
check_metri_cubi = lambda metri_cubi: MAX_METRI_CUBI if (metri_cubi > MAX_METRI_CUBI) else (
    MIN_METRI_CUBI if (metri_cubi < MIN_METRI_CUBI) else metri_cubi)


def display_ambiente(ambiente):
    return ambiente.name + ': ' + str(ambiente.cubic_meters) + ' m^3'


# ---------------------------------------------------------------------------------------
class Prodotto:
    '''Prodotto'''
    CONCENTRAZIONE_STANDARD = 1
    MAX_MILLILITRI = 1000
    MIN_MILLILITRI = 1

    def __init__(self, nome: str, concentrazione: int, data_scadenza: datetime.date = None, lotto=[]):
        self.concentrazione = concentrazione
        self.nome = nome
        # non serve lotto e data di scadenza nn obbligatori
        self.lotto = lotto
        self.data_scadenza = data_scadenza
        self._millilitri = 1

    @property
    def millilitri(self):
        return self._millilitri
    @millilitri.setter
    def millilitri(self, metri_cubi):
        self._millilitri = metri_cubi * self.get_concentrazione()

    def configura(self, lotto, concentrazione):
        self.concentrazione = concentrazione
        self.lotto = lotto

    def format_data_scadenza(self):
        if self.data_scadenza == None:
            data_scad = None
        else:
            data_scad = self.data_scadenza.strftime("%d/%m/%y")
        return data_scad

    def get_concentrazione(self):
        if self.concentrazione == None:
            return Prodotto.CONCENTRAZIONE_STANDARD
        else:
            return self.concentrazione

    def __dict__(self):
        return OrderedDict(
            {NOME_PRODOTTO: self.nome, CONCENTRAZIONE: self.concentrazione,
             DATA_SCADENZA: self.format_data_scadenza(), LOTTO: self.lotto
             })

    def __repr__(self):
        return str({NOME_PRODOTTO: self.nome, DATA_SCADENZA: self.format_data_scadenza(), LOTTO: self.lotto,
                    CONCENTRAZIONE: self.concentrazione})

    def __str__(self):
        return self.nome + ": " + str(self.concentrazione)
