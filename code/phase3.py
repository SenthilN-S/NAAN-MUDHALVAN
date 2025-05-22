class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

class Supplier:
    def __init__(self, name, product, supply_amount):
        self.name = name
        self.product = product
        self.supply_amount = supply_amount

    def restock(self):
        self.product.update_quantity(self.supply_amount)
        print(f"{self.name} supplied {self.supply_amount} units of {self.product.name}.")

class Order:
    def __init__(self, product, order_quantity):
        self.product = product
        self.order_quantity = order_quantity

    def process_order(self):
        if self.product.quantity >= self.order_quantity:
            self.product.update_quantity(-self.order_quantity)
            print(f"Order processed for {self.order_quantity} units of {self.product.name}.")
        else:
            print(f"Insufficient stock for {self.product.name}. Only {self.product.quantity} units available.")

# Example Usage
product1 = Product("Laptop", 50)
supplier1 = Supplier("TechSupplier Inc.", product1, 20)

order1 = Order(product1, 30)
order2 = Order(product1, 50)

order1.process_order()
supplier1.restock()
order2.process_order()

