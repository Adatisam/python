num = cont = soma = 0
while True:
    num = int(input('Digite o número [999] para parar: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))

from datetime import date
atual = date.today().year 
totmaior = 0
totmenor = 0
for pes in range(1, 2):
    nasc = int(input('Em que ano a {}˚ pessoa nasceu? '.format(pes)))
    idade = atual = nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas de maior.'.format(totmaior))
print('Ao todo tivemos {} pessoas de menor.'.format(totmenor))