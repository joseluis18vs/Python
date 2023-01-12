from bs4 import BeautifulSoup
from Operaciones.obtenerHTML import get_html


def get_board():
    """

    :return:
    """
    try:
        str_html = get_html()  # Puede agregar una url, en este caso al dejarlo son argumento leerá la url por defecto.
        try:
            bs = BeautifulSoup(str_html, 'html.parser')
            bs.find('table', {'id': 'tb1_1139'})
            return bs.findAll('tr')
        except NameError as e:
            print(e)
    except NameError as e:
        print(e)
