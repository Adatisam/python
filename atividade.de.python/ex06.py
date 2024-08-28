nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}' .format(media))
if media >= float(60):
    print('Aprovado')
else:
    print('Reprovado') 