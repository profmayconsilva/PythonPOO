from rich import print, inspect

class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depositos
    """
    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'A conta com o id {self.id} pertence ao Sr. {self.titular} e possui o saldo de R$ {self.saldo:,.2f}'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito (Conta {self.id}): R$ {self.saldo:,.2f}')
    def sacar(self, valor):
        if valor > self.saldo:
            print (f"Saque de R$ {valor:,.2f} não foi atualizado por motivo de SALDO INSUFICIENTE")
            return
        self.saldo -= valor
        print(f'Sacado (Conta {self.id}): R$ {self.saldo:,.2f}')

c = ContaBancaria(12, "José", 1200)
inspect(c)