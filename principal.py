from funcoes import *
from estilos import *

# Fase inicial do programa.
inicio()
yv = pegarLink('Insira o link aqui ➤ ')

# Lista de itags.
listaitags = []

# Print das streams do vídeo.
cabecalho('Código     Tipo/Ext.     Res/Tam.', 3, 4)
for x in yv.streams:
    if x.resolution:
        c(f'  {x.itag:<11}{x.mime_type:<14}{x.resolution:<10}'.center(42), 5)
    if x.abr:
        c(f'  {x.itag:<11}{x.mime_type:<14}{x.abr:<10}'.center(42), 5)
    listaitags.append(x.itag)
linha(3)


# Inserção da itag desejada.
while True:
    try:
        n = int(input(c('Insira o código desejado ➤ ', 3, True)))
    except:
        c('Insira somente números.', 1)
    else:
        if n in listaitags:
            break
        else:
            c('Insira somente um dos códigos da tabela.', 1)

# Pegando a itag e fazendo o Download.
ys = yv.streams.get_by_itag(n)
cabecalho('Fazendo o download...', 5, 4)
sleep(2)

# Mensagens de erro ou sucesso.
x = 2
while x != 3:
    try:
        ys.download()
    except:
        print('\033[31mNão foi possível baixar o arquivo.\033[m')
        print(f'\033[33mVou tentar novamente, pela {x}° vez (MÁX 3).\033[m')
        sleep(4)
        x += 1
        if x == 3:
            print('\033[31mNão foi possível baixar o arquivo.\033[m')
    else:
        print('\033[32mO arquivo foi baixado com sucesso. Verifique a mesma pasta onde abriu o script.')
        break
