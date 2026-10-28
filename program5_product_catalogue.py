# Tuple-Based Product Catalogue Audit

products = [
    ("P101", 100, 20),
    ("P102", 250, 5),
    ("P103", -50, 10),
    ("P104", 500, 0),
    ("P105", 150, 8)
]

total_inventory_value = 0
minimum_stock = 10

for product in products:
    product_id, price, quantity = product

    print("Product ID:", product_id)

    if product_id == "" or price <= 0 or quantity < 0:
        print("Invalid product record")

    else:
        inventory_value = price * quantity
        total_inventory_value += inventory_value

        print("Price: Rs.", price)
        print("Stock Quantity:", quantity)
        print("Inventory Value: Rs.", inventory_value)

        if quantity < minimum_stock:
            print("Replenishment Required")

print("Total Inventory Value: Rs.", total_inventory_value)
