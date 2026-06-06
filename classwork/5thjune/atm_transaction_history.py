transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Current balance
balance = sum(transactions)

# Separate deposits and withdrawals
deposits = []
withdrawals = []

for t in transactions:
    if t > 0:
        deposits.append(t)
    else:
        withdrawals.append(t)

# Largest deposit and withdrawal
largest_deposit = deposits[0]
for d in deposits:
    if d > largest_deposit:
        largest_deposit = d

largest_withdrawal = withdrawals[0]
for w in withdrawals:
    if w < largest_withdrawal:
        largest_withdrawal = w

# Output
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
