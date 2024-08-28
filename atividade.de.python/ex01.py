vel = int(input('Digite a velocidade: '))
multa = float((vel/4) * 7.50)
if vel < 80: 
    print('Tudo certo, dirija com segurança"')
else:
    print('MULTADO, sua conta é de R${:.2f}' .format(multa))
