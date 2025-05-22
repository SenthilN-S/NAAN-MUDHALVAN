import datetime

# ------------------ Data Structures ------------------

class Product:
    def __init__(self, product_id, name, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, supplier_id, name):
        self.supplier_id = supplier_id
        self.name = name

class Order:
    def __init__(self, order_id, product_id, quantity, order_date):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.order_date = order_date

# ------------------ Data Stores ------------------

products = {}
suppliers = {}
orders = []

# ------------------ Functions ------------------

def add_supplier():
    sid = input("Enter Supplier ID: ")
    name = input("Enter Supplier Name: ")
    suppliers[sid] = Supplier(sid, name)
    print(f"Supplier {name} added.")

def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    qty = int(input("Enter Initial Quantity: "))
    sid = input("Enter Supplier ID: ")
    if sid not in suppliers:
        print("Supplier does not exist.")
        return
    products[pid] = Product(pid, name, qty, sid)
    print(f"Product {name} added.")

def view_inventory():
    print("\n--- Inventory ---")
    for pid, product in products.items():
        supplier_name = suppliers[product.supplier_id].name
        print(f"{pid}: {product.name} | Qty: {product.quantity} | Supplier: {supplier_name}")

def process_order():
    pid = input("Enter Product ID: ")
    if pid not in products:
        print("Product not found.")
        return
    qty = int(input("Enter Order Quantity: "))
    product = products[pid]
    if product.quantity >= qty:
        product.quantity -= qty
        oid = f"O{len(orders)+1}"
        orders.append(Order(oid, pid, qty, datetime.date.today()))
        print(f"Order {oid} processed.")
    else:
        print("Not enough stock available.")

def view_orders():
    print("\n--- Orders ---")
    for order in orders:
        pname = products[order.product_id].name
        print(f"{order.order_id}: {pname} | Qty: {order.quantity} | Date: {order.order_date}")

# ------------------ Main Menu ------------------

def main():
    while True:
        print("\n--- Supply Chain Management ---")
        print("1. Add Supplier")
        print("2. Add Product")
        print("3. View Inventory")
        print("4. Process Order")
        print("5. View Orders")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_supplier()
        elif choice == '2':
            add_product()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            process_order()
        elif choice == '5':
            view_orders()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
