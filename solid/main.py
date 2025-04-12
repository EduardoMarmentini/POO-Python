# Importando as classes necessárias
from models.product import Product
from services.orderService import Order, LoyalCustomerDiscount
from services.notification import EmailNotion
from repositories.productRepository import ProductRepository


# Injetando dependências
repo = ProductRepository()
notion = EmailNotion()
order = Order()
discount = LoyalCustomerDiscount()

# Criando produtos
products = [
    {"Name": "Pizza", "Price": 30.00},
    {"Name": "Refrigerante", "Price": 5.00},
    {"Name": "Sorvete", "Price": 12.00},
    {"Name": "Salada", "Price": 15.00},
    {"Name": "Frango Assado", "Price": 40.00},
    {"Name": "Sopa", "Price": 20.00},
    {"Name": "Bolo", "Price": 25.00},
    {"Name": "Café", "Price": 8.00},
    {"Name": "Suco Natural", "Price": 10.00},
    {"Name": "Sanduíche", "Price": 18.00},
]

# Definindo headers
header_name = f"{' Bem-vindo ao MarmitasLanches! '.center(50, '=')}"
header_menu = f"{'ID'.ljust(5)} | {'Nome'.ljust(20)} | {'Preço'.rjust(10)}"

print("-" * len(header_name))
print(header_name)
print("-" * len(header_name))

# Salvando produtos
for prod in products:
    product = Product(prod["Name"], prod["Price"])
    repo.save(product)

#Exibe os produtos
print("Produtos disponíveis:")
print("=" * len(header_menu))

print(header_menu)
print("=" * len(header_menu))
repo.listAll()
print("=" * len(header_menu))


# Salvando pedido
while True:
    product_id = int(input("Digite o ID do produto desejado (0 para finalizar): "))
    print("-" * len(header_name))

    if product_id == 0:
        break

    product = repo.findById(product_id)
    order.add_item(product)
    
    print(f"Produto '{product.name}' adicionado ao pedido.")
    print("-" * len(header_name))

order.show_items()
print("-" * len(header_name))

# Aplicando desconto
total_with_discount = discount.apply(order.calc_tot())


print(f"Total com desconto: R${total_with_discount:.2f}")
print("-" * len(header_name))

# Finalizando pedido e enviando a notificação
notion.send(f"Pedido finalizado! Total com desconto: R${total_with_discount:.2f}")