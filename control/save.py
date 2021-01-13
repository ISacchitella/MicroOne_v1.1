import json
import os
from pprint import pprint
from shutil import move, copy
from sys import stderr
from time import sleep
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import psutil
import string
from collections import OrderedDict
from datetime import date, datetime

from control.literals import INFO, PRODOTTI, AMBIENTI, DATA_SCADENZA, NOME_PRODOTTO, CONCENTRAZIONE, LOTTO, DATA, \
    PRODOTTO, AMBIENTE, METRI_CUBI, VERSIONE
from model.ambiente_prodotto import Ambiente, Prodotto
from model.dispositivo import IS_RASPBERRY
from view import recap_info_window


def get_file_path(file_name, extension='.json'):
    path = os.path.join(os.path.abspath(os.getcwd()), file_name + extension)
    if not os.path.exists(path):
        inizializer = {INFO: {}, PRODOTTI: [], AMBIENTI: []}
        json.dump(inizializer[file_name], open(path, 'w+'), indent=1)
    return path


def save_all(ambienti, prodotti, info):
    save_ambienti(ambienti)
    save_prodotti(prodotti)
    save_info(info)


def save_ambienti(ambienti):
    with open(get_file_path(AMBIENTI), 'w') as f:
        json.dump(ambienti, f, indent=1)


def save_prodotti(prodotti):
    with open(get_file_path(PRODOTTI), 'w') as f:
        json.dump([p.__dict__() for p in prodotti], f, indent=1)


def load_ambienti():
    list = json.load(open(get_file_path(AMBIENTI)))
    ambienti = []
    for ambiente in list:
        ambienti.append(Ambiente(ambiente[0], ambiente[1]))
    return ambienti


def load_prodotti():
    list = json.load(open(get_file_path(PRODOTTI)))
    prodotti = []
    for prodotto in list:
        if prodotto[DATA_SCADENZA] != None:
            data_scadenza_l = prodotto[DATA_SCADENZA].split('/')
            data_scadenza = date(int(data_scadenza_l[2]) + 2000, int(data_scadenza_l[1]), int(data_scadenza_l[0]))
        else:
            data_scadenza = None
        prodotti.append(Prodotto(prodotto[NOME_PRODOTTO], prodotto[CONCENTRAZIONE], data_scadenza=data_scadenza,
                                 lotto=prodotto[LOTTO]))
    return prodotti


def load_info():
    info = json.load(open(get_file_path(INFO)))
    if not isinstance(info, dict):
        return OrderedDict()
    elif len(info) == 0:
        return OrderedDict()
    else:
        return OrderedDict(info)


def save_info(info):
    json.dump(info, open(get_file_path(INFO), 'w'), indent='\t')


def poweroff():
    if not IS_RASPBERRY:
        return
    os.system("sudo poweroff")
    # os.system("shutdown now -h")  # shut down the Pi -h is or -r will reset


def close_timer(window, stop, arresta=None):
    stop()
    if arresta != None:
        arresta()
    window.close()


def display_riepilogo(riepilogo):
    formatted_str = ""
    formatted_str += f"Treatment Date: {riepilogo[DATA]} \n"
    formatted_str += f"Selected Product:{riepilogo[PRODOTTO][NOME_PRODOTTO]}\n"
    formatted_str += f"Concentration: {str(riepilogo[PRODOTTO][CONCENTRAZIONE])}\n"
    formatted_str += f"Product Expiry Date: {riepilogo[PRODOTTO][DATA_SCADENZA]}\n"
    formatted_str += f"Batch Number: {riepilogo[PRODOTTO][LOTTO][0]}\n"
    formatted_str += f"Selected Room: {riepilogo[AMBIENTE]} \n"
    formatted_str += f"Cubic Meters: {riepilogo[METRI_CUBI]} \n"
    return formatted_str


def format_info(info):
    formatted_str = ""
    formatted_str += f"Serial Number {info['serial_number'].upper()}\n"
    formatted_str += f"Version {info[VERSIONE]}\n"
    return formatted_str


FSTYPE_USB_TYPES = ('NTFS', 'FAT32', 'exFAT', 'HFS+', 'EXT2', 'EXT3', 'EXT4', 'ext4', 'fuseblk')


def download_status_timer(timer, seconds, label):
    seconds[0] -= 1
    if seconds[0] <= 0:
        timer.stop()
        label.setStyleSheet("color: rgb(85,170,0); \n"
                            "font-size: 20px; \n")
        label.setText("Download Completed!")


def copy_info(label, btn):
    disk_partitions = unpack(psutil.disk_partitions())
    pprint(disk_partitions)
    try:
        usb_drive_path = next((drive["mountpoint"] for drive in disk_partitions if
                               drive["fstype"] in FSTYPE_USB_TYPES and any(
                                   x in ['removable', 'relatime'] for x in drive["opts"].split(','))))
    except:
        usb_drive_path = None
    print(usb_drive_path)
    if usb_drive_path not in [None, '']:

        btn.setStyleSheet('''background-color: rgb(0, 134, 255);
                 color: rgb(255, 255, 255);
                 border-radius:10px;
             ''')

        timer = QtCore.QTimer()
        seconds = [20]
        timer.timeout.connect(lambda: download_status_timer(timer,seconds, label))
        timer.start(2000)
        try:
            copy(get_file_path(INFO), usb_drive_path)
        except:
            label.setStyleSheet("color: rgb(255, 0, 0); \n"
                                "font-size: 20px; \n")
            label.setText("Error Download!")
        else:
            label.setStyleSheet("color: rgb(226, 119, 30); \n"
                                "font-size: 20px; \n")
            label.setText("Ongoing Download...")
            timer.startTimer(seconds[0], timerType=Qt.VeryCoarseTimer)
        # os.rename(usb_drive_path + "logMicroOne.json",usb_drive_path + 'info.txt')
    else:
        print('Error: No Pen Drive Found', file=stderr)
        label.setStyleSheet("color: rgb(255,0,0); \n"
                            "font-size: 20px; \n")
        label.setText("Plug in a Pen Drive!")



def get_system_info():
    system_info = OrderedDict()
    system_info['boot_time'] = datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S %d/%m/%y")
    # system_info['os'] = platform.uname()._asdict()
    # system_info['os']['architecture'] = platform.architecture()
    # system_info['measures'] = ['bytes', 'mega bits (MB)', 'seconds', 'Mhz', 'celsius']
    # system_info['disk'] = {
    #     'available_drives': ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)],
    #     'disk_usage': psutil.disk_usage('/')._asdict(),
    #     'disk_partitions': psutil.disk_partitions(),
    #     'disk_io_counters': psutil.disk_io_counters()._asdict()  # perdisk=True
    # }
    # system_info['memory'] = {
    #     'virtual_memory': psutil.virtual_memory()._asdict(),
    #     'swap_memory': psutil.swap_memory()._asdict()
    # }
    # system_info['cpu'] = {
    #     "total_cores": psutil.cpu_count(logical=True),
    #     "physical_cores": psutil.cpu_count(logical=False),
    #     'frequency': psutil.cpu_freq()._asdict(),
    #     'cpu_times': psutil.cpu_times()._asdict()
    # }
    # if platform.system() == 'Linux':
    #     system_info['os']['linux_details'] = platform._syscmd_uname('-a')
    # system_info['users'] = psutil.users()
    # # system_info['network'] = {
    # #     'net_connections': psutil.net_connections(),
    # #     'net_io_counters': psutil.net_io_counters(),
    # #     'net_if_addrs': psutil.net_if_addrs(),
    # #     'net_if_stats': psutil.net_if_stats(),
    # # }
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
    print('test')
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
