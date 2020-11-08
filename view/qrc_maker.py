from os import system
from shutil import move

if __name__ == '__main__':
    PCUIC5 = 'pyrcc5 '
    qrc_path = 'img_resources.qrc'
    py_path = qrc_path.split('.')[0] + '_rc.py'
    command = PCUIC5 + qrc_path + ' -o ' + py_path
    system(command)
    move(py_path, '../' + py_path)
