import os
from tkinter import filedialog


'''
Regresa la dirección de un archivo especifico.
'''


def get_file():
    return filedialog.askopenfilename()


'''
Regresa la dirección de un directorio especifico.
'''


def get_directory():
    return filedialog.askdirectory()


'''
Regresa una lista de los archivos contenidos en la dirección del directorio proporcionado 
'''


def directory_file_list(path):
    return os.listdir(path)
