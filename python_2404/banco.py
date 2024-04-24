# Requisitos:
# Nome do titular
# número da conta
#CPF
#Saldo
#O que faz:
#Saque
#Depósito
#Transferência 

class Conta():
    
    def __init__(self, titular, cpf, tipo_conta, num_conta, saldo = 0):
        self.titular = titular
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.num_conta = num_conta
        self.saldo = saldo
        self.extrato = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            saida = 'Deposito feito na conta no valor de: ' + str(valor)
            self.extrato.append(saida)
            # self.saldo+self.saldo + valor

        else:
            print("Valor inválido!")
    
    def saque(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        elif self.saldo >= valor:
            self.saldo -= valor
            saida = 'Saque de: ' + str(valor)
        else:
            print('Valor do saque é maior do que o saldo!')

    def transferencia(self, destinatario, valor):
        if valor > 0 and self.saldo >valor:
            destinatario.saldo += valor
            saida = 'Transferência de: ' + str(valor) + 'para conta do ' + destinatario.titular
            self.extrato.append(saida)
            self.saque(valor)

        else:
            print("Valor inválido ou saldo insulficiente")

    def verificar_extrato(self):
        print('Extrato')
        for item in self.extrato:
            print(item)

conta1 = Conta("kati", "8347983693", "Corrente", "00055-5")
conta2 = Conta("Caroline","11111111", "Corrente", "00044-4")

print(conta1.saldo)
conta1.deposito(2000)
print(conta1.saldo)
conta1.saque(100)
print(conta1.saldo)
conta1.transferencia(conta2, 2.50)
print('c1', conta1.saldo)
print('c2', conta2.saldo)

conta1.verificar_extrato()
