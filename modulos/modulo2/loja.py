print('===' *10)
print('LOJA')
print('===' *10)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/PIX')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra parcelado em 2x de R${:.2f}'. format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 /100)
    totoparc = int(input('Quantas parcelas? '))
    parcela = total / totoparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'. format(totoparc, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA DE PAGAMENTO')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'. format(preco, total))