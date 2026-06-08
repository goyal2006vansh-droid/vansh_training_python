# Employee performance scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp, "-", score)

# 2. Count employees needing improvement (score < 60)
count = 0
for score in performance.values():
    if score < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# 3. Find the top performer
top_emp = max(performance, key=performance.get)
print("Top Performer:", top_emp, "-", performance[top_emp])

# 4. Calculate average performance score
average = sum(performance.values()) / len(performance)
print("Average Performance Score:", round(average, 2))

# 5. Create separate lists
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif 75 <= score <= 89:
        good.append(emp)
    elif 60 <= score <= 74:
        average_list.append(emp)
    else:
        poor.append(emp)

print("\nExcellent (>= 90):", excellent)
print("Good (75-89):", good)
print("Average (60-74):", average_list)
print("Poor (< 60):", poor)
