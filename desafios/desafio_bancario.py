menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))
        if deposito < 0:
            print("Operação inválida!")
        else:
            saldo += deposito
            print(f"O depósito de R$ {deposito:.2f} foi realizado com sucesso!")
            print(f"Seu saldo atual é de R$ {saldo:.2f}.")
            extrato += f"Depósito de R$ {deposito:2f}, "

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))

        if saque <= 0:
            print("Operação inválida! Informe o valor de saque.")

        elif saque <= limite and saque <= saldo and numero_saques < LIMITE_SAQUES:
            saldo -= saque
            print(f"O saque de R$ {saque:.2f} foi realizado com sucesso!")
            print(f"Seu saldo atual é de R$ {saldo:.2f}.")
            extrato += f"Saque de R$ {saque:2f}, "
            numero_saques += 1

        elif saque > saldo:
            print("Saldo insuficiente!")

        elif saque > limite:
            print("Saque acima do limite diário!")

        else:
            print("Você atingiu seu limite diário de saques!.")

    elif opcao == "e":
        print(extrato, f"Saldo de R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
