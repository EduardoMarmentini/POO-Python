class Product:
    _id_counter = 1

    def __init__(self, name, price):
        self.id = Product._id_counter
        Product._id_counter += 1
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Produto(id={self.id}, nome='{self.name}', preco={self.price})"
