print('-=-' * 10)
print('Analisador de Trângulos')
print('-=-' * 10)
lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos PODEM formar um TRIANGULO!')
else:
    print('Os segmentos NÃO PODEM formar um TRIANGULO!')

