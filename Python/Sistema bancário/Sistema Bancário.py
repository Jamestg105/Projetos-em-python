saldo = 0.0
extrato = []
saques_realizados = 0
LIMITE_SAQUES = 3
LIMITE_POR_SAQUE = 500.0

while True:
    print("\n=== Sistema Bancário ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Visualizar Extrato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = input("Digite o valor para depósito: R$ ")
        if valor.replace('.', '', 1).isdigit():
            valor = float(valor)
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado.")
            else:
                print("Valor inválido para depósito.")
        else:
            print("Entrada inválida. Digite um número válido.")
    elif opcao == '2':
        if saques_realizados >= LIMITE_SAQUES:
            print("Você atingiu o limite de 3 saques.")
            continue
        valor = input("Digite o valor para saque: R$ ")
        if valor.replace('.', '', 1).isdigit():
            valor = float(valor)
            if valor <= 0:
                print("Valor inválido para saque.")
            elif valor > saldo:
                print("Saldo insuficiente.")
            elif valor > LIMITE_POR_SAQUE:
                print(f"O saque máximo permitido por operação é R$ {LIMITE_POR_SAQUE:.2f}.")
            else:
                saldo -= valor
                saques_realizados += 1
                extrato.append(f"Saque: R$ {valor:.2f}")
                print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Entrada inválida. Digite um número válido.")
    elif opcao == '3':
        print("\n=== Extrato ===")
        if len(extrato) == 0:
            print("Nenhuma movimentação realizada.")
        else:
            for item in extrato:
                print(item)
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == '4':
        print("Saindo do sistema. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")
