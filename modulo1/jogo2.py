from random import randint
comput = randint(0, 10)
print('Sou seu computador... Acabei de pesnsar em um número entre 0 a 10. ')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    if jogador == comput:
        acertou = True
        print('O número que pensei foi {}'.format(comput))
print('Acabou')