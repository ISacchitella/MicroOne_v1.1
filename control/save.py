import json
import os, platform
from shutil import move, copy
from sys import stderr

import psutil
import string
from collections import OrderedDict
from datetime import date, datetime

from model.ambiente_prodotto import Ambiente, Prodotto


def get_file_path(file_name, extension='.json'):
    path = os.path.join(os.path.abspath(os.getcwd()), file_name + extension)
    if not os.path.exists(path):
        inizializer = {'info': {}, 'prodotti': [], 'ambienti': []}
        json.dump(inizializer[file_name], open(path, 'w+'), indent=1)
    return path


def save_all(ambienti, prodotti, info):
    save_ambienti(ambienti)
    save_prodotti(prodotti)
    save_info(info)


def save_ambienti(ambienti):
    with open(get_file_path('ambienti'), 'w') as f:
        json.dump(ambienti, f, indent=1)


def save_prodotti(prodotti):
    with open(get_file_path('prodotti'), 'w') as f:
        json.dump([p.__dict__() for p in prodotti], f, indent=1)


def load_ambienti():
    list = json.load(open(get_file_path('ambienti')))
    ambienti = []
    for ambiente in list:
        ambienti.append(Ambiente(ambiente[0], ambiente[1]))
    return ambienti


def load_prodotti():
    list = json.load(open(get_file_path('prodotti')))
    prodotti = []
    for prodotto in list:
        if prodotto['data_scadenza'] != None:
            data_scadenza_l = prodotto['data_scadenza'].split('/')
            data_scadenza = date(int(data_scadenza_l[2]) + 2000, int(data_scadenza_l[1]), int(data_scadenza_l[0]))
        else:
            data_scadenza = None
        prodotti.append(Prodotto(prodotto['nome'], prodotto['concentrazione'], data_scadenza = data_scadenza, lotto=prodotto['lotto']))
    return prodotti


def load_info():
    info = json.load(open(get_file_path('info')))
    if not isinstance(info, dict):
        return OrderedDict()
    elif len(info) == 0:
        return OrderedDict()
    else:
        return OrderedDict(info)


def save_info(info):
    json.dump(info, open(get_file_path('info'), 'w'), indent='\t')


def poweroff():
    os.system("shutdown /s /t 1")
    # os.system("shutdown now -h")  # shut down the Pi -h is or -r will reset


def display_riepilogo(riepilogo):
    formatted_str = ""
    formatted_str += f"Data del trattamento: {riepilogo['data']} \n"
    formatted_str += f"Prodotto selezionato:{riepilogo['prodotto']['nome']}\n"
    formatted_str += f"Concentrazione: {str(riepilogo['prodotto']['concentrazione'])}\n"
    formatted_str += f"Data Scadenza Prodotto: {riepilogo['prodotto']['data_scadenza']}\n"
    formatted_str += f"Lotto: {riepilogo['prodotto']['lotto'][0]}\n"
    formatted_str += f"Ambiente selezionato: {riepilogo['ambiente']} \n"
    formatted_str += f"Metri cubi inseriti: {riepilogo['metri_cubi']} \n"
    return formatted_str


def format_info(info):
    formatted_str = ""
    formatted_str += f"Serial Number {info['serial_number'].upper()}\n"
    formatted_str += f"Versione {info['versione']}\n"
    return formatted_str


FSTYPE_USB_TYPES = ('NTFS', 'FAT32', 'exFAT', 'HFS+', 'EXT2', 'EXT3', 'EXT4')


def copy_info():
    disk_partitions = unpack(psutil.disk_partitions())
    try:
        usb_drive_path = next((drive["mountpoint"] for drive in disk_partitions if
                           drive["fstype"] in FSTYPE_USB_TYPES and 'removable' in drive["opts"].split(',')))
    except:
        usb_drive_path = None
    if usb_drive_path not in [None, '']:
        copy(get_file_path('info'), usb_drive_path)
    else:
        print('Error: Nessuna Pen Drive Trovata', file=stderr)
        # raise FileNotFoundError


def get_system_info():
    system_info = OrderedDict()
    system_info['boot_time'] = datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S %d/%m/%y")
    system_info['os'] = platform.uname()._asdict()
    system_info['os']['architecture'] = platform.architecture()
    system_info['measures'] = ['bytes', 'mega bits (MB)', 'seconds', 'Mhz', 'celsius']
    system_info['disk'] = {
        'available_drives': ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)],
        'disk_usage': psutil.disk_usage('/')._asdict(),
        'disk_partitions': psutil.disk_partitions(),
        'disk_io_counters': psutil.disk_io_counters()._asdict()  # perdisk=True
    }
    system_info['memory'] = {
        'virtual_memory': psutil.virtual_memory()._asdict(),
        'swap_memory': psutil.swap_memory()._asdict()
    }
    system_info['cpu'] = {
        "total_cores": psutil.cpu_count(logical=True),
        "physical_cores": psutil.cpu_count(logical=False),
        'frequency': psutil.cpu_freq()._asdict(),
        'cpu_times': psutil.cpu_times()._asdict()
    }
    if platform.system() == 'Linux':
        system_info['os']['linux_details'] = platform._syscmd_uname('-a')
    system_info['users'] = psutil.users()
    # system_info['network'] = {
    #     'net_connections': psutil.net_connections(),
    #     'net_io_counters': psutil.net_io_counters(),
    #     'net_if_addrs': psutil.net_if_addrs(),
    #     'net_if_stats': psutil.net_if_stats(),
    # }
    return unpack(system_info)


def isnamedtupleinstance(x):
    _type = type(x)
    bases = _type.__bases__
    if len(bases) != 1 or bases[0] != tuple:
        return False
    fields = getattr(_type, '_fields', None)
    if not isinstance(fields, tuple):
        return False
    return all(type(i) == str for i in fields)


def unpack(obj):
    if isinstance(obj, dict):
        return {key: unpack(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [unpack(value) for value in obj]
    elif isnamedtupleinstance(obj):
        return {key: unpack(value) for key, value in obj._asdict().items()}
    elif isinstance(obj, tuple):
        return tuple(unpack(value) for value in obj)
    else:
        return obj


if __name__ == '__main__':
    pass
    # poweroff()
    # print(Ambiente('p',9)._asdict())
    # print()
    # save_prodotti([Prodotto('test', date.today())])
    # p = load_prodotti()
    # print(p, type(p[0].data_scadenza))
    # info = {'serial_number': 'ABC5690', 'version': 1.0}
    # save_info(info)
    # print(load_info())
    # prodotti = load_prodotti()
    # print(prodotti, type(prodotti[0]))
    # ambienti = load_ambienti()
    # print(ambienti, type(ambienti[0]))
