distancia = float(input('Qual a distância da sua viagem? (km) '))
if distancia < 200:
    distancia1 = float(distancia * 0.50)
    print('O valor da viagem fica R${:.2f}' .format(distancia1))
else:
    distancia1 = float(distancia * 0.45)
    print('O valor da viagem fica R${:.2f}' .format(distancia1))
print('Boa viajem!')