# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
product1 = ("P001", "Smartphone X", 799.99, 21, "Mobile Phones")
product2 = ("P002", "Laptop Pro", 1299.99, 9, "Laptops")
product3 = ("P003", "Bluetooth Speaker", 89.99, 20, "Audio")
product4 = ("P004", "Tablet Plus", 499.99, 7, "Tablets")
product5 = ("P005", "Wireless Headphones", 199.99, 6, "Audio")

# TODO 2: Create an inventory list containing all product tuples
inventory = [product1, product2, product3, product4, product5]

# TODO 3: Display all products
print("\nCurrent Inventory:")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 4: Access specific elements
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

print("\n\nAccessing Specific Products:")
print("-" * 60)
print("First product:", first_product)
print("Last product:", last_product)
print("Third product name:", third_product_name)
print("Second product price:", second_price)
print("Second product quantity:", second_quantity)

# TODO 5: Use slicing to get subsets
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)
print("First three products:", first_three)
print("Middle products:", middle_products)
print("All except first:", all_except_first)

# TODO 6: Add new products to inventory
product6 = ("P006", "Gaming Laptop", 1499.99, 4, "Laptops")
product7 = ("P007", "Smartwatch", 299.99, 12, "Wearables")

inventory.append(product6)
inventory.append(product7)

print("\n\nAdding New Products:")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 7: Remove a product
removed_product = inventory.pop(2)

print("\n\nRemoving a Product:")
print("-" * 60)
print("Removed product:", removed_product)
print("Updated inventory:")
for product in inventory:
    print(product)

# TODO 8: Insert a product at a specific position
product8 = ("P008", "Noise Cancelling Earbuds", 249.99, 8, "Audio")
inventory.insert(1, product8)

print("\n\nInserting a Product:")
print("-" * 60)
for product in inventory:
    print(product)

# REDO TODO 4 and 5
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

# TODO 9: Create category lists
mobile_phones = []
laptops = []
audio = []

for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_phones.append(product)
    elif product[4] == "Laptops":
        laptops.append(product)
    elif product[4] == "Audio":
        audio.append(product)

print("\n\nProducts by Category:")
print("-" * 60)
print("Mobile Phones:", mobile_phones)
print("Laptops:", laptops)
print("Audio:", audio)

# TODO 10: Calculate inventory statistics
total_products = len(inventory)
total_value = sum(product[2] * product[3] for product in inventory)
product_names = [product[1] for product in inventory]
product_prices = [product[2] for product in inventory]

print("\n\nInventory Statistics:")
print("-" * 60)
print("Total products:", total_products)
print("Total value:", total_value)
print("Product names:", product_names)
print("Product prices:", product_prices)

# TODO 11: Expensive products
expensive_products = [product for product in inventory if product[2] > 500]

print("\n\nExpensive Products (> $500):")
print("-" * 60)
print(expensive_products)

# TODO 12: Low stock alert
low_stock = [product for product in inventory if product[3] < 5]

print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)
print(low_stock)

# TODO 13: Price lists
original_prices = [product[2] for product in inventory]
discounted_prices = [price * 0.9 for price in original_prices]

print("\n\nPrice Lists:")
print("-" * 60)
print("Original prices:", original_prices)
print("Discounted prices:", discounted_prices)

# TODO 14: Product name formatting
uppercase_names = [product[1].upper() for product in inventory]
product_codes = [product[0][:3] + product[1][:3] for product in inventory]

print("\n\nFormatted Product Names:")
print("-" * 60)
print("Uppercase names:", uppercase_names)
print("Product codes:", product_codes)

# TODO 15: Using loops
mobile_count = 0
laptop_value = 0
most_expensive = inventory[0]

for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_count += 1
    if product[4] == "Laptops":
        laptop_value += product[2] * product[3]
    if product[2] > most_expensive[2]:
        most_expensive = product

print("\n\nLoop-Based Analysis:")
print("-" * 60)
print("Mobile phone count:", mobile_count)
print("Laptop value:", laptop_value)
print("Most expensive product:", most_expensive)

# TODO 16: Using conditionals
restock_list = []
high_value_items = []
price_ranges = {"under_100":0, "100_to_500":0, "over_500":0}

for product in inventory:
    price = product[2]
    quantity = product[3]

    if quantity < 5:
        restock_list.append(product)

    if price > 500 and quantity > 10:
        high_value_items.append(product)

    if price < 100:
        price_ranges["under_100"] += 1
    elif price <= 500:
        price_ranges["100_to_500"] += 1
    else:
        price_ranges["over_500"] += 1

print("\n\nConditional Analysis:")
print("-" * 60)
print("Restock list:", restock_list)
print("High value items:", high_value_items)
print("Price ranges:", price_ranges)

# TODO 17: Functions
def calculate_product_value(product):
    return product[2] * product[3]

def find_products_by_category(inventory, category):
    return [product for product in inventory if product[4] == category]

def apply_discount(inventory, discount_percent):
    new_inventory = []
    for product in inventory:
        new_price = product[2] * (1 - discount_percent/100)
        new_inventory.append((product[0], product[1], new_price, product[3], product[4]))
    return new_inventory

total_inventory_value = sum(calculate_product_value(p) for p in inventory)
audio_products = find_products_by_category(inventory, "Audio")
discounted_inventory = apply_discount(inventory, 15)

print("\n\nFunction-Based Operations:")
print("-" * 60)
print("Total inventory value:", total_inventory_value)
print("Audio products:", audio_products)
print("Discounted inventory:", discounted_inventory)

# TODO 18: Inventory report
def generate_inventory_report(inventory):
    total_products = len(inventory)
    total_value = sum(p[2] * p[3] for p in inventory)
    categories = list(set([p[4] for p in inventory]))
    low_stock = [p for p in inventory if p[3] < 5]
    average_price = sum(p[2] for p in inventory) / total_products

    return {
        "total_products": total_products,
        "total_value": total_value,
        "categories": categories,
        "low_stock": low_stock,
        "average_price": average_price
    }

report = generate_inventory_report(inventory)

print("\n\nComprehensive Inventory Report:")
print("-" * 60)
print(report)