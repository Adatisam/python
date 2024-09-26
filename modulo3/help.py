c = ''
def ajuda(com):
    help(com)

def titulo(msg, cor= 0 ):
    tam =len(msg)
    print('-='*tam)
    print(f'{msg}')
    print('-='*tam)


comando = ''
while True:
    titulo('SISTEMA E AJUDA Py HELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else: 
        ajuda(comando)
    titulo('ATÉ LOGO')