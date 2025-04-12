from datetime import datetime

class Order:
    def __init__(self):
        self.itens = []


    def add_item(self, product):
        self.itens.append(product)


    def calc_tot(self):
        return sum([product.price for product in self.itens])

class OrderPrinter:
    def show(order: Order, discount: 'Discount' = None):
        items = order.items
        if not items:
            print("Pedido vazio!")
            return

        max_name_length = max(len(item.name) for item in items)
        line_length = max_name_length + 40

        print("Itens do Pedido:")
        print("=" * line_length)
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. Produto: {item.name:<{max_name_length}} | Preço: R${item.price:>7.2f}")
        print("=" * line_length)
        total = order.calc_total(discount)
        print(f"Total: R${total:.2f}")       


# Aqui esta sendo aplicado o principio de Opend/Closed Principle (OCP)

# Aqui possuo uma classe base Discount e duas classes que herdam dela
class Discount:
    def apply(self, value):
        return value


# Em geral aqui eu posso ter uma classe que aplica o desconto de acordo com o tipo de cliente, isso me permite adicionar novos tipos de desconto sem modificar o código existente, apenas criando novas classes que herdam de Discount.
class LoyalCustomerDiscount(Discount):
    def apply(self, value):
        return value * 0.9


# Nesta desconto verifico se a data que estou aplicando o desconto é a Black Friday, se for aplico o desconto de 50% no valor do produto.
class BlackFridayDiscount(Discount):
    def is_valid_today(self):
        today = datetime.now()
        return today.month == 11 and today.weekday() == 4 and (today.day + 7 > 30)


    def apply(self, value):
        if self.is_valid_today():
            return value * 0.5
        return value