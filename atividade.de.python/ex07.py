from datetime import date
ano = int(input('digite o ano que quer analisar e veremos se ele é bixesto ou não: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print('É BIXESTO!')
else: 
    print('NÃO É BIXESTO!')
print('Espero poder ter ajudado.')