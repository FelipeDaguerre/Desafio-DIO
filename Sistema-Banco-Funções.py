import textwrap

def menu():
    menu_text = """
    [1]\tDepósitos
    [2]\tSaques
    [3]\tExtrato
    [4]\tCriar Novo Usuário
    [5]\tCriar nova conta
    [6]\tListar contas
    [9]\tSair

    : """
    return input(textwrap.dedent(menu_text))

def depositos(saldo, extrato):
    deposito = float(input("Quanto deseja depositar? - "))
    if deposito <= 0:
        print("@ Valor inválido @")
    else:
        saldo += deposito
        extrato += f"Depósito: R${deposito:.2f}\n"
        print(f" -- \n\nDepósito realizado com sucesso no valor de - R${deposito:.2f} -- ")
    return saldo, extrato

def saques(saldo, extrato, numero_saque, saque_limite):
    saque = float(input("Quanto deseja sacar? "))
    if numero_saque == saque_limite:
        print("Limite de saques diários atingidos, são permitidos apenas 3 por dia.")
    elif saque > saldo:
        print(f"Saldo insuficiente, seu saldo total é R$ {saldo:.2f}")
    elif saque > 500:
        print("O saque deve ser de no máximo 500 reais.")
    elif saque <= 0:
        print("Valor inválido.")
    else:
        saldo -= saque
        extrato += f"\tSaque: R${saque:.2f}\n"
        numero_saque += 1
        print(f"-- Saque realizado com sucesso no valor de R${saque:.2f} --")
    return saldo, extrato, numero_saque

def exibir_extrato(saldo, extrato):
    print("-------------------------------------------------")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nO seu saldo atual é de R${saldo:.2f}")
    print("-------------------------------------------------")    

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\n @ Usuário já existente @ ")
        return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade / sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(" -- Usuário criado com sucesso. -- ")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if not usuario:
        print("\n @ Usuário não encontrado @ ")
        return
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    contas.append(conta)
    print("\n -- Conta criada com sucesso. -- ")

def listar_contas(contas):
    for conta in contas:
        print('-' * 50)
        print(f"Agência:\t{conta['agencia']}")
        print(f"C/C:\n\n{conta['numero_conta']}")
        print(f"Titular:\n{conta['usuario']['nome']}")

def main():
    AGENCIA = '0001'
    saldo = 0
    saque_limite = 3
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato = depositos(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saque = saques(saldo, extrato, numero_saque, saque_limite)
                
        elif opcao == "3":
            exibir_extrato(saldo, extrato)

                
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "9":
            print("Volte sempre!")
            break

        else:
            print("Opção inválida, selecione uma opção de 1 a 9")

main()
