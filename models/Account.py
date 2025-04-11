class Account:
    _contas = []

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._status = True
        Account._contas.append(self)

    def __str__(self):
        return f"Titular: {self._titular} | Saldo: {self._saldo:.2f} | Status: {self.status}"

        
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