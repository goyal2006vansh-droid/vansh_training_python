# Password Security Analyzer
#strings 
strong = 0
medium = 0
weak = 0

for i in range(15):
    print("\nPassword", i + 1)
    password = input("Enter password: ")

    upper = lower = digits = special = 0
    vowels = consonants = 0

    # Count characters
    for ch in password:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1

        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    # Length and spaces check
    length_ok = len(password) >= 8
    has_space = " " in password

    # Password strength
    if length_ok and upper > 0 and lower > 0 and digits > 0 and special > 0:
        strength = "Strong"
        strong += 1
    elif length_ok and (upper > 0 or lower > 0) and digits > 0:
        strength = "Medium"
        medium += 1
    else:
        strength = "Weak"
        weak += 1

    # Repeated characters
    repeated = []
    for ch in password:
        if password.count(ch) > 1 and ch not in repeated:
            repeated.append(ch)

    # Most frequent character
    max_char = ""
    max_count = 0
    for ch in password:
        if password.count(ch) > max_count:
            max_count = password.count(ch)
            max_char = ch

    # Display results
    print("Uppercase Letters :", upper)
    print("Lowercase Letters :", lower)
    print("Digits            :", digits)
    print("Special Characters:", special)
    print("Minimum Length OK :", length_ok)
    print("Contains Spaces   :", has_space)
    print("Password Strength :", strength)
    print("Repeated Characters:", repeated)
    print("Vowels            :", vowels)
    print("Consonants        :", consonants)
    print("Most Frequent Character:", max_char)

# Final Report
print("\n===== SECURITY REPORT =====")
print("Total Passwords Analyzed :", 15)
print("Strong Passwords :", strong)
print("Medium Passwords :", medium)
print("Weak Passwords   :", weak)
