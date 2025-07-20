import random

usuarios = []

def cadastrar_usuario():
    cpf = input("Digite o CPF do usuário (somente números): ").strip()
    nome = input("Digite o nome do usuário: ").strip()

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado!")
            return

    usuario = {
        'cpf': cpf,
        'nome': nome,
        'contas': []
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

def gerar_numero_conta():
    # Gera 4 dígitos aleatórios e junta com '0001'
    aleatorio = ''.join(str(random.randint(0,9)) for _ in range(4))
    return "0001" + aleatorio

def cadastrar_conta():
    cpf = input("Digite o CPF do usuário para criar a conta: ").strip()
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break

    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    # Se quiser permitir múltiplas contas, remova a checagem abaixo
    if usuario['contas']:
        print("Usuário já possui conta cadastrada.")
        return

    numero_conta = gerar_numero_conta()

    conta = {
        'numero': numero_conta,
        'saldo': 0.0,
        'extrato': []
    }
    usuario['contas'].append(conta)
    print(f"Conta {numero_conta} cadastrada para o usuário {usuario['nome']}.")

# ... o restante do código fica igual ...

def encontrar_conta():
    cpf = input("Digite o CPF do usuário: ").strip()
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break

    if not usuario:
        print("Usuário não encontrado.")
        return None, None

    if not usuario['contas']:
        print("Usuário não possui conta cadastrada.")
        return usuario, None

    # Como só há uma conta, pega a primeira
    conta = usuario['contas'][0]
    return usuario, conta

def depositar():
    usuario, conta = encontrar_conta()
    if not conta:
        return

    try:
        valor = float(input("Digite o valor para depósito: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("Valor deve ser positivo.")
        return

    conta['saldo'] += valor
    conta['extrato'].append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def sacar():
    usuario, conta = encontrar_conta()
    if not conta:
        return

    try:
        valor = float(input("Digite o valor para saque: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    if valor <= 0:
        print("Valor deve ser positivo.")
        return

    if valor > conta['saldo']:
        print("Saldo insuficiente.")
        return

    conta['saldo'] -= valor
    conta['extrato'].append(f"Saque: R$ {valor:.2f}")
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def exibir_extrato():
    usuario, conta = encontrar_conta()
    if not conta:
        return

    print("\n=== Extrato ===")
    if not conta['extrato']:
        print("Nenhuma movimentação.")
    else:
        for registro in conta['extrato']:
            print(registro)
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")

def main():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1 - Cadastrar Usuário")
        print("2 - Cadastrar Conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Visualizar Extrato")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            cadastrar_conta()
        elif opcao == '3':
            depositar()
        elif opcao == '4':
            sacar()
        elif opcao == '5':
            exibir_extrato()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
