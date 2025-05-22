import datetime
import random
from collections import defaultdict

# Inventory Management
class Inventory:
    def __init__(self):
        self.stock = defaultdict(int)

    def add_stock(self, product, quantity):
        self.stock[product] += quantity
        print(f"Added {quantity} units of {product}. Current stock: {self.stock[product]}")

    def remove_stock(self, product, quantity):
        if self.stock[product] >= quantity:
            self.stock[product] -= quantity
            print(f"Removed {quantity} units of {product}. Remaining stock: {self.stock[product]}")
        else:
            print(f"Insufficient stock for {product}.")

    def get_stock(self, product):
        return self.stock.get(product, 0)

# Order Management
class OrderManager:
    def __init__(self, inventory):
        self.inventory = inventory
        self.orders = []

    def place_order(self, product, quantity):
        stock = self.inventory.get_stock(product)
        if stock >= quantity:
            self.inventory.remove_stock(product, quantity)
            order = {
                'product': product,
                'quantity': quantity,
                'date': datetime.datetime.now()
            }
            self.orders.append(order)
            print(f"Order placed: {product} x {quantity}")
        else:
            print(f"Cannot place order: Not enough {product} in stock.")

# Demand Forecasting (Simple Moving Average)
class DemandForecaster:
    def __init__(self, sales_history):
        self.sales_history = sales_history  # {product: [sales_data_list]}

    def forecast(self, product, window=3):
        data = self.sales_history.get(product, [])
        if len(data) < window:
            return sum(data) / len(data) if data else 0
        return sum(data[-window:]) / window

# Supplier Management
class SupplierManager:
    def __init__(self):
        self.suppliers = {}

    def add_supplier(self, name, products):
        self.suppliers[name] = products
        print(f"Supplier {name} added with products: {products}")

    def get_suppliers_for_product(self, product):
        return [name for name, products in self.suppliers.items() if product in products]

# Example Usage
if __name__ == "__main__":
    inventory = Inventory()
    order_manager = OrderManager(inventory)
    supplier_manager = SupplierManager()

    # Simulate some suppliers
    supplier_manager.add_supplier("Global Supply Inc.", ["Widget", "Gadget"])
    supplier_manager.add_supplier("Tech Parts Co.", ["Gadget", "Sensor"])

    # Add inventory
    inventory.add_stock("Widget", 50)
    inventory.add_stock("Gadget", 30)

    # Place orders
    order_manager.place_order("Widget", 20)
    order_manager.place_order("Gadget", 40)  # Should fail

    # Forecasting
    sales_data = {
        "Widget": [10, 15, 20, 25, 30],
        "Gadget": [5, 10, 15]
    }
    forecaster = DemandForecaster(sales_data)
    print("Forecast for Widget:", forecaster.forecast("Widget"))
    print("Forecast for Gadget:", forecaster.forecast("Gadget"))

    # Supplier lookup
    print("Suppliers for Gadget:", supplier_manager.get_suppliers_for_product("Gadget"))
