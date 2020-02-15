from os import listdir, path, system

from utils import functions
from utils.menu import instructions


def start():
    instructions()

    path_file = None
    while True:
        path_file = input("Ingresa la ruta al archivo: ")
        if path.isdir(path_file):
            break
        else:
            print('La ruta está mal.')

    file_name = None
    while True:
        dir_files = listdir(path_file)

        for index, f in enumerate(dir_files):
            print(f"{index}. {f}")

        file_name = int(input("Ingresa el número del archivo: "))
        file_name = dir_files[file_name]
        if path.isfile(path.join(path_file, file_name)):
            break
        else:
            print('Incorrecto.')


if __name__ == '__main__':
    start()
