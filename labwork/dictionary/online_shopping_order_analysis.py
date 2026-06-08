# Product sales data
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products sold more than 20 times
print("Products sold more than 20 times:")
for product, qty in sales.items():
    if qty > 20:
        print(product, "-", qty)

# 2. Best-selling product
best_product = max(sales, key=sales.get)
print("\nBest-selling product:", best_product, "-", sales[best_product])

# 3. Least-selling product
least_product = min(sales, key=sales.get)
print("Least-selling product:", least_product, "-", sales[least_product])

# 4. Total products sold
total_sold = sum(sales.values())
print("Total products sold:", total_sold)

# 5. Products requiring promotion (sales < 15)
promotion = []
for product, qty in sales.items():
    if qty < 15:
        promotion.append(product)

print("Products requiring promotion:", promotion)

# 6. Count products having sales between 10 and 30
count = 0
for qty in sales.values():
    if 10 <= qty <= 30:
        count += 1

print("Number of products with sales between 10 and 30:", count)
