from collections import namedtuple, OrderedDict
from datetime import datetime

'''Timer misurato in secondi'''
TEMPO_ALLONTANAMENTO = 10
'''Ambiente'''
Ambiente = namedtuple('Ambiente', ['nome', 'metri_cubi'])
MAX_METRI_CUBI = 3000
MIN_METRI_CUBI = 1
check_metri_cubi = lambda metri_cubi: MAX_METRI_CUBI if (metri_cubi > MAX_METRI_CUBI) else (
    MIN_METRI_CUBI if (metri_cubi < MIN_METRI_CUBI) else metri_cubi)


def display_ambiente(ambiente):
    return ambiente.nome + ': ' + str(ambiente.metri_cubi) + ' m^3'


# ---------------------------------------------------------------------------------------
class Prodotto:
    '''Prodotto'''
    CONCENTRAZIONE_STANDARD = 28

    def __init__(self, nome: str, concentrazione: int, data_scadenza: datetime.date = None, lotto=[]):
        self.concentrazione = concentrazione
        self.nome = nome
        # non serve lotto e data di scadenza nn obbligatori
        self.lotto = lotto
        self.data_scadenza = data_scadenza

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
            {'nome': self.nome, 'concentrazione': self.concentrazione,
             'data_scadenza': self.format_data_scadenza(), 'lotto': self.lotto
             })

    def __repr__(self):
        return str({'nome': self.nome, 'data_scadenza': self.format_data_scadenza(), 'lotto': self.lotto,
                    'concentrazione': self.concentrazione})

    def __str__(self):
        return repr(self)
