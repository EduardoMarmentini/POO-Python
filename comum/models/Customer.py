from models.Account import Account


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
            self._conta = Account(self._nome, 0)
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