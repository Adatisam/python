from time import sleep
import random
numero = [0, 1, 2, 3, 4, 5]
numal = random.choice(numero)
print('-=-' *10)
print('Jogaremos adivinhação escolha o número e tente adivinhar!')
num = int(input('Digite um número de 0 a 5: '))
print('-=-' *10)
print('PROCESSANDO...')
sleep(1)
if num == numal:
    print('ACERTOOU!')
else: 
    print('ERROOU!')
print('o número escolhido foi {}' .format(numal))