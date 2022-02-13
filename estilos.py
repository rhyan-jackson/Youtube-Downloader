from time import sleep
cores = [
    '\033[m',  # 0 ➤ limpa
    '\033[31m',  # 1 ➤ vermelho
    '\033[33m',  # 2 ➤ amarelo
    '\033[34m',  # 3 ➤ azul escuro
    '\033[36m',  # 4 ➤ azul claro
    '\033[32m',  # 5 ➤ verde
]


def inicio():
    cabecalho('Youtube Downloader', 3, 4)
    c('Bem-vindo ao Youtube Downloader, um projeto feito por Rhyan.', 3)
    sleep(1.5)
    c('Para baixar um vídeo é só inserir o link abaixo.', 4)
    sleep(1.5)
    c('< Modelos de como colocar o link >', 3)
    c('Assim: https://www.youtube.com/watch?v=2kqdlAYNEzk\n'
      'Ou assim: www.youtube.com/watch?v=2kqdlAYNEzk', 4)
    linha(4)


def c(msg, idcor=0, retorna=False):
    if retorna:
        return f'{cores[idcor]}{msg}{cores[0]}'
    else:
        print(f'{cores[idcor]}{msg}{cores[0]}')


def linha(cor=0, tam=42):
    c('-' * tam, cor)


def cabecalho(msg, corletras=0, corlinha=0, tam=42):
    linha(corlinha, tam)
    c(msg.center(tam), corletras)
    linha(corlinha, tam)


def sair():
    c('Saindo do programa, obrigado por ter utilizado nossos serviços.', 1)
    exit()
