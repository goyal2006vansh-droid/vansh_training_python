units = {
    "House101": 320, "House102": 180, "House103": 510,
    "House104": 275, "House105": 150, "House106": 430,
    "House107": 220, "House108": 390, "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house)

# 2. Highest-consuming house
highest = max(units, key=units.get)
print("\nHighest Consumption:", highest, f
