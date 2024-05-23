menu = """
[1] Depositos
[2] Saques
[3] Extrato
[4] Sair

Escolha a opção desejada: """

saldo = 0
saque_limite = 3
extrato = ""
numero_saque = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Quanto deseja depositar? - "))
        if deposito <= 0:
            print("Valor inválido")
        else:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print(f"Deposito realizado com sucesso no valor de - R${deposito}")


    elif opcao == "2":
        saque = float(input("Quanto deseja sacar? "))

        if numero_saque == saque_limite:
            print("Limite de saques diários atingidos, são permitidos apenas 3 por dia.")
        elif saque > saldo:
            print(f"Saldo insuficiente, seu saldo total é R$ {saldo}")
        elif saque > 500:
            print("O saque deve ser de no máximo 500 reais.")
        elif saque <=0:
            print("Valor inválido.")

        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saque += 1
            print(f"Saque realizado com sucesso no valor de {saque}")

        
    elif opcao == "3":
        print("-------------------------------------------------")
        print(f"Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nO seu saldo atual é de R${saldo:.2f}")
        print("-------------------------------------------------")


    elif opcao == "4":
        print("\nVolte sempre!")
        break


    else:
        print("Opção inválida, selecione uma opção de 1 a 4")



