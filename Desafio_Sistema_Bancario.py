menu = '''

            ********* MENU *********
    
    [S] - Sacar
    [D] - Depositar
    [E] - Extrato
    [Q] - Sair

********* Selecione a operação desejada *********

=> '''

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    operacao = input(menu)

    # DEPÓSITO

    if operacao == "D" or operacao == "d":
        valor = float(input("\nInforme o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"

        else:
            print("\nOperação falhou! Valor informado é inválido!")

    # SAQUE

    elif operacao == "S" or operacao == "s":
        valor = float(input("\nInforme o valor do saque: "))

        if valor > limite_valor_saque:
            print("\nValor do saque superior que o limite permitido!")

        elif valor > saldo:
            print("\nSaldo insuficiente!")

        elif numero_de_saques >= LIMITE_DE_SAQUES:
            print("\nNúmero de saques diarios foi excido")
        
        elif valor > 0:

            saldo -= valor
            extrato += f"Valor do saque: {valor:.2f}\nSaldo: {saldo:.2f}" 
            numero_de_saques += 1

    # EXTRATO

    elif operacao == "E" or operacao == "e":

        print("\n******* EXTRATO *******")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    # SAIR

    elif operacao == "Q" or operacao == "q":
        break

    else:
        print("\nOpção inválida! Seleciona uma das opções informadas!")