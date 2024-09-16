from random import randint
v = 0
while True:
    num = int(input('Digite um número: '))
    pc = randint(0, 10)
    total = pc + num
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('Você jogou {} e o computador jogou {} o número era {}'.format(num, pc, total))
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P': 
        if num % 2 == 0:
            print('VENCEU!')
        else:
            print('PERDEU!')
    elif tipo == 'I':
        if num % 2 == 1:
            print('VENCEU!')
        else:
            print('PERDEU!')
    jogar = str(input('Jogar novamente? [S/N]: ')).strip().upper()[0]
    if jogar == 'N':
        break
print('Fim')
    