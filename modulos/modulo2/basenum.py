num = int(input("Digite um número inteiro: "))
print("escolha uma das bases para conversão")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} covertido para BINÁRIO é igual a {}". format( num, bin(num)[2:]))
elif opcao == 2:
    print("{} covertido para OCTAL é igual a {}". format( num, oct(num)[2:]))
elif opcao == 3:
    print("{} covertido para HEXADECIMAL é igual a {}". format( num, hex(num)[2:]))
else:
    print("Opção inválida tente novamente.")
