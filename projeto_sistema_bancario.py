import textwrap

class ContaBancaria:
    def __init__(self, limite=500, limite_saques=3):
        self.saldo = 0
        self.limite = limite
        self.extrato = ""
        self.numero_saques = 0
        self.limite_saques = limite_saques

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return True
        else:
            return False

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo or excedeu_limite or excedeu_saques or valor <= 0:
            return False

        self.saldo -= valor
        self.extrato += f"Saque: R$ {valor:.2f}\n"
        self.numero_saques += 1
        return True

    def exibir_extrato(self):
        print("\n================ EXTRATO =======================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("================================================")

def exibir_menu():
    menu = """
    ========================================
    |          MENU - BANK                 |
    ========================================
    | [d] Depositar                        |
    | [s] Sacar                            |
    | [e] Extrato                          |
    | [q] Sair                             |
    ========================================

    => """
    return input(menu)

# Programa principal
conta = ContaBancaria()

while True:
    opcao = exibir_menu()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            if conta.depositar(valor):
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Erro: Digite apenas números para o valor.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            if conta.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! Verifique o saldo, limite e número de saques.")
        except ValueError:
            print("Erro: Digite apenas números para o valor.")

    elif opcao == "e":
        conta.exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")