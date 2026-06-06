stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = []
restock = []
available = 0
high_stock = []

for qty in stock:
    if qty == 0:
        out_of_stock.append(qty)

    if qty < 10:
        restock.append(qty)

    if qty > 0:
        available += 1

    if qty >= 15:
        high_stock.append(qty)

print("Out of Stock Products:", out_of_stock)
print("Products Needing Restock:", restock)
print("Available Products:", available)
print("Stock >= 15:", high_stock)
