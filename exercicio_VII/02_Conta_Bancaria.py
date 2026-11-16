class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
        else:
            self.__saldo += valor
            print("Depósito realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")


# Teste obrigatório
conta = ContaBancaria("João", 100.00)

conta.depositar(50.00)
conta.sacar(30.00)

print(f"Titular: {conta.titular}")
print(f"Saldo final: R$ {conta.saldo:.2f}")