class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depositos
    """
    def __init__(self, id, titular, saldo = 0):
        self.id = id # público (+)
        self._titular = titular # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f'Conta {self.id} criado com sucesso. Saldo atual: R${self.__saldo:,.2f}')

    def __str__(self):
        return f'Estado atual: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito (Conta {self.id}) de R${valor:.2f}, Saldo atual R$ {self.__saldo:,.2f}')
    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print (f"Saque de R$ {valor:,.2f} não foi atualizado por motivo de SALDO INSUFICIENTE")
            return
        self.__saldo -= valor
        print(f'Saque (Conta {self.id}) de R${valor:.2f}: R$ {self.__saldo:,.2f}')

