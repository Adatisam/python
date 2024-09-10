nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}' .format(media))
if media >= float(6):
    print('Aprovado'.upper())
elif 7 > media >= 5:
    print('Recuperação'.upper())
else:
    print('Reprovado'.upper()) 