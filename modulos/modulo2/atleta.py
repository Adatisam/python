from datetime import date
num = int(input("Ano de nascimento: "))
ano = date.today().year
nasc = ano - num
print('O atleta de {} anos'. format(nasc))
if nasc <= 9:
    print('MIRIM')
elif 10 <= nasc <= 14:
    print('INFANTIL')
elif 15 <= nasc <= 19:
    print('JÚNIOR')
elif 20 <= nasc <= 25:
    print('SÊNIOR')
else:
    print('MASTER')