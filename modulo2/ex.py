from datetime import date
nasc = int(input("Digite sua data de nascimento: "))
data = date.today().year
idade = data - nasc
print("Quem nasceu em {} tem {} anos em {}.". format(nasc, idade, data))
if idade == 19:
    print("Você deve se alistar imediatamente!")
elif idade < 19:
    anos = 19 - idade
    serv = data + anos
    print("Ainda falta {} anos para o alistamento". format(anos))
    print("Você servirá no ano de {}". format(serv))
elif idade > 19:
    anos = idade - 19
    serv = data - anos
    print("Você já cumpriu suas obrigações militares, ou deveria ter se alistado a {} anos". format(anos))
    print("Seu ano de Serviço foi {}". format(serv))
