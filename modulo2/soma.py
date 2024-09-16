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

num = cont = soma = 0
num = int(input('Digite o número [999] para parar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite o número [999] para parar: '))
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))