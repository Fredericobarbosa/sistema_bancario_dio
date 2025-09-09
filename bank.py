menu="""
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(" MENU ".center(20,"="))
    opcao = int(input(menu))

    if opcao == 1:
        print("DEPÓSITO".center(20,"="))
        valor = float(input("Insira o valor a ser depositado: "))

        if (valor>0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Saldo atual: R$ {saldo:.2f}")
        elif (valor<0):
            print("Valor para depósito inválido!")

    elif opcao == 2:
        print("SAQUE".center(20,"="))
        valor = float(input("Insira o valor a ser sacado: "))

        if (valor>0) and (valor<=saldo) and (valor<=500) and (numero_saques<LIMITE_SAQUES):
            print(f"Valor sacado: R$ {valor:.2f}")
            saldo -= valor
            numero_saques+=1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saldo atual: R$ {saldo:.2f}")
        elif (valor > saldo):
            print("Não será possível efetuar o saque por falta de saldo!")
        elif (valor>500):
            print("Valor solicitado indisponivel limite máximo por saque R$500,00!")
        elif (numero_saques>=LIMITE_SAQUES):
            print("Limite de saques diários atingido!")
        else:
            print("Valor para saque inválido!")

    elif opcao == 3:
        print("EXTRATO".center(20,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(20*"=")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")