# Email Analyzer

domain_count = {}
invalid_emails = []

for i in range(20):
    email = input(f"Enter email {i+1}: ")

    # Check validity
    valid = (email.count('@') == 1 and '.' in email and ' ' not in email)

    if not valid:
        invalid_emails.append(email)
        print("Invalid Email")
        continue

    # Extract username and domain
    username, domain = email.split('@')

    # Extract extension
    extension = domain.split('.')[-1]

    # Count digits in username
    digit_count = 0
    for ch in username:
        if ch.isdigit():
            digit_count += 1

    # Count special characters in username
    special_count = 0
    for ch in username:
        if not ch.isalnum():
            special_count += 1

    # Store domain count
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

    # Display details
    print("\nUsername :", username)
    print("Domain   :", domain)
    print("Extension:", extension)
    print("Digits in Username :", digit_count)
    print("Special Characters :", special_count)

# Invalid Emails
print("\n===== INVALID EMAILS =====")
for email in invalid_emails:
    print(email)

# Domain Report
print("\n===== DOMAIN REPORT =====")
for domain in domain_count:
    print(domain, "->", domain_count[domain], "users")
