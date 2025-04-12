from models.Customer import Customer
from models.Account import Account


def main():
    Customer("João", 30, "Rua A, 123", "123.456.789-00", "Engenheiro")
    Customer("Maria", 28, "Rua B, 456", "987.654.321-00", "Médica")

    Customer.showCustomers()
    Customer.createAccount(Customer._clientes[0])

    print(Customer._clientes[0].conta)

    Customer._clientes[0].conta.changeStatus(Customer._clientes[0].conta)

    print(Customer._clientes[0].conta)

    Account.showAccounts()


if __name__ == "__main__":
    main()
