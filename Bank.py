class ContaBancaria:
    _contas = []

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._status = True
        ContaBancaria._contas.append(self)


    @property
    def titular(self):
        return self._titular


    @property
    def saldo(self):
        return self._saldo


    @property
    def status(self):
        return "☑" if self._status else "☐"


    @classmethod
    def changeStatus(cls, conta):
        conta._status = not conta._status


    @classmethod
    def showAccounts(cls):
        print("Contas criadas:")
        print("=" * 55)
        print(f"{'|Titular'.ljust(25)} | {'Saldo'.rjust(15)} | {'Status'.center(10)}|")
        print("-" * 55)

        for account in cls._contas:
            print(f"|{account.titular.ljust(25)} | {str(f'{account.saldo:.2f}').rjust(15)} | {str(account.status).center(10)}|")
            print("-" * 55)
        print("=" * 55)


class Customer:
    _clientes = []

    def __init__(self, nome, idade, endereco, cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao
        self._conta = None
        Customer._clientes.append(self)


    @property
    def nome(self):
        return self._nome


    @property
    def idade(self):
        return self._idade


    @property
    def endereco(self):
        return self._endereco


    @property
    def cpf(self):
        return self._cpf


    @property
    def profissao(self):
        return self._profissao


    @property
    def conta(self):
        return self._conta


    def createAccount(self):
        if not self._conta:
            self._conta = ContaBancaria(self._nome, 0)
        return self._conta


    @classmethod
    def showCustomers(cls):
        print("Clientes cadastrados:")
        print("=" * 70)
        print(f"{'|Nome'.ljust(25)} | {'Idade'.rjust(5)} | {'CPF'.center(20)} | {'Profissão'.center(10)}|")
        print("-" * 70)

        for customer in cls._clientes:
            print(f"|{customer.nome.ljust(25)} | {str(customer.idade).rjust(5)} | {customer.cpf.center(20)} | {customer.profissao.center(10)}|")
            print("-" * 70)
        print("=" * 70)


customer1 = Customer("João", 30, "Rua A, 123", "123.456.789-00", "Engenheiro")
customer2 = Customer("Maria", 28, "Rua B, 456", "987.654.321-00", "Médica")


Customer.showCustomers()

customer1.createAccount()
customer2.createAccount()


ContaBancaria.showAccounts()

ContaBancaria.changeStatus(customer1.conta)
ContaBancaria.changeStatus(customer2.conta)

ContaBancaria.showAccounts()