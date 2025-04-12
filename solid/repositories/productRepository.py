from interfaces.dbInterface import ProductInterface

class ProductRepository(ProductInterface):
    def __init__(self):
        self.products = []


    def save(self, product):
        self.products.append(product)


    def update(self, product):
        for pos, prod in enumerate(self.produtos):
            if prod.id == product.id:
                self.produtos[pos] = product
                return
            
        print("[ERRO] Produto não encontrado.")


    def delete(self, product_id):
        self.produtos = [p for p in self.produtos if p.id != product_id]


    def findById(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
            
        print("[ERRO] Produto não encontrado.")


    def listAll(self):
        for product in self.products:
            print(f"{str(product.id).ljust(5)} | {product.name.ljust(20)} | R${str(f'{product.price:.2f}').rjust(10)}")
            
        return 