menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    try:
        opcao = int(input(menu))
    except ValueError:
        print("Opção inválida. Por favor, insira um número correspondente à operação desejada.")
        continue

    if opcao == 1:
        try:
            valor = float(input("Informe o valor do depósito (use ponto para decimais, ex: 100.50): "))
        except ValueError:
            print("Valor inválido! Por favor, insira um valor numérico.")
            continue

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado deve ser positivo.")

    elif opcao == 2:
        try:
            valor = float(input("Informe o valor do saque (use ponto para decimais, ex: 100.50): "))
        except ValueError:
            print("Valor inválido! Por favor, insira um valor numérico.")
            continue

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado deve ser positivo.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 4:
        print("Operação finalizada. Até a próxima!")
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")
