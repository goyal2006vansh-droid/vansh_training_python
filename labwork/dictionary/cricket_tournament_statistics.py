runs = {
    "Virat": 645, "Rohit": 512, "Gill": 698, "Rahul": 435,
    "Hardik": 278, "Pant": 534, "Surya": 389, "Jadeja": 301,
    "Iyer": 455, "KL": 410
}

# 1. Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player, score in runs.items():
    if score > 500:
        print(player)

# 2. Orange Cap winner
orange_cap = max(runs, key=runs.get)
print("\nOrange Cap Winner:", orange_cap, f"({runs[orange_cap]})")

# 3. Lowest scorer
lowest = min(runs, key=runs.get)
print("Lowest Scorer:", lowest, f"({runs[lowest]})")

# 4. Total runs scored
print("Total Tournament Runs:", sum(runs.values()))

# 5. Players scoring below 400
below_400 = [player for player, score in runs.items() if score < 400]
print("Players Scoring Below 400:", below_400)

# 6. Count players scoring between 400 and 600
count = sum(1 for score in runs.values() if 400 <= score <= 600)
print("Players Between 400 and 600 Runs:", count)
