casa = float(input("Valor da casa: R$"))
salario = float(input("salario do comprador: R$"))
financiamento = int(input("Quantos anos de finânciamento? "))
prestacao = casa / (financiamento * 12)
minimo = salario * (30/100)
print("Para pagar uma casa de R${:.2f} em {} anos". format(casa, financiamento), end='')
print(" a prestação será de R${:.2f}". format(prestacao))
print("COMPARANDO R${:.2f} - R${:.2f}". format(prestacao, minimo))
if prestacao <= minimo:
    print("Emprestimo pode ser CONCEDIDO!")
#elif prestacao == minimo:
    #print("Emprestimo ainda pode ser CONCEDIDO, mas vale resaltar que esta batendo no seu LIMITE!")
else :
    print("Emprestimo NEGADO!")