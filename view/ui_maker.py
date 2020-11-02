import glob
from os import system

if __name__ == '__main__':
    PCUIC5 = 'pyuic5 -x '
    for ui_path in glob.glob("**/*", recursive=True):
        if ui_path.endswith('.' + 'ui'):
            py_path = ui_path.split('.')[0] + '.py'
            command = PCUIC5 + ui_path + ' -o ' + py_path
            system(command)
