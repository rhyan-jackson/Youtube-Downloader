import requests
from pytube import YouTube
from estilos import *


def pegarLink(msg):
    while True:
        a = str(input(c(msg, 3, True)))
        if not (a.startswith('https://') or a.startswith('http://')):
            a = 'https://' + a
        try:
            requests.get(a)
        except:
            print('\033[31mO link inserido não é válido ou sua conexão com a internet não é suficiente.\033[m')
        else:
            try:
                yv = YouTube(a)
            except:
                print('\033[31mO link inserido não é válido ou sua conexão com a internet não é suficiente.\033[m')
            else:
                return yv
