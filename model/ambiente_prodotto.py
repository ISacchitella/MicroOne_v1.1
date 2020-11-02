from collections import namedtuple, OrderedDict
from datetime import datetime
'''Timer misurato in secondi'''
TEMPO_ALLONTANAMENTO = 10
'''Ambiente'''
Ambiente = namedtuple('Ambiente', ['nome', 'metri_cubi'])
MAX_METRI_CUBI = 3000
MIN_METRI_CUBI = 1
check_metri_cubi = lambda metri_cubi: MAX_METRI_CUBI if (metri_cubi > MAX_METRI_CUBI) else (MIN_METRI_CUBI if ( metri_cubi < MIN_METRI_CUBI) else metri_cubi)
def display_ambiente(ambiente):
    return ambiente.nome + ': ' + str(ambiente.metri_cubi) + ' m^3'
#---------------------------------------------------------------------------------------
class Prodotto:
    '''Prodotto'''
    CONCENTRAZIONE_STANDARD = 28

    def __init__(self, nome: str, data_scadenza: datetime.date, lotto=None, concentrazione=None):
        self.concentrazione = concentrazione
        self.nome = nome
        # non serve lotto e data di scadenza nn relativi al prodotto
        self.lotto = lotto
        self.data_scadenza = data_scadenza

    def configura(self, lotto, concentrazione):
        self.concentrazione = concentrazione
        self.lotto = lotto

    def get_concentrazione(self):
        if self.concentrazione == None:
            return Prodotto.CONCENTRAZIONE_STANDARD
        else:
            return self.concentrazione

    def __dict__(self):
        return OrderedDict(
            {'nome': self.nome, 'data_scadenza': self.data_scadenza.strftime("%d/%m/%y"), 'lotto': self.lotto,
             'concentrazione': self.concentrazione})

    def __repr__(self):
        return str({'nome': self.nome, 'data_scadenza': self.data_scadenza.strftime("%d/%m/%y"), 'lotto': self.lotto,
                    'concentrazione': self.concentrazione})

    def __str__(self):
        return repr(self)
