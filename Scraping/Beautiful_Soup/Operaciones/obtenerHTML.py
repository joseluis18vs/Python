from Recursos.urls import list_
from Recursos.headers import header
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def get_html(url=list_['bolsa']):
    """
    Realiza petición segura http.
    :return: Regresa estructura html de la web solicitada, en formato de cadena de texto (str).
    """
    try:
        html_ = Request(url, None, header)
        return urlopen(html_).read()
    except HTTPError as e:
        print('Error en petición http.')
        print(e)
    except URLError as e:
        print('Error en el funcionamiento del servidor.')
        print(e)
