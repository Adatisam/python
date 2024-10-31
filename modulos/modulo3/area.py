def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')
print('Controle de terrenos')
print('-'*20)
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimetno: '))
area(l, c)
