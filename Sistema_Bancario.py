import datetime

# Variáveis globais do sistema bancário
saldo = 0
limite_saques = 3
limite_saque = 500
extrato = ""
numero_saques = 0

def depositar(valor):
    global saldo
    global extrato

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito. Insira um valor positivo.")

def sacar(valor):
    global saldo
    global limite_saques
    global limite_saque
    global numero_saques
    global extrato

    if valor > 0:
        if numero_saques < limite_saques:
            if valor <= limite_saque:
                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo insuficiente.")
            else:
                print(f"Limite de saque por operação é de R$ {limite_saque:.2f}")
        else:
            print("Limite de saques diários atingido.")
    else:
        print("Valor inválido para saque. Insira um valor positivo.")

def visualizar_extrato():
    global saldo
    global extrato

    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print("\n========== Extrato ==========")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=============================")

def main():
    global numero_saques

    while True:
        # Reinicia o número de saques diários à meia-noite (00:00)
        if datetime.datetime.now().hour == 0:
            numero_saques = 0

        print("\n=====  Python Bank =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor a depositar: "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a sacar: "))
            sacar(valor)
        elif opcao == "3":
            visualizar_extrato()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
