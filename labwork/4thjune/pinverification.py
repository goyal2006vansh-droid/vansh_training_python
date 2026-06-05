# Valid PIN
correct_pin = "1234"

while True:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try Again.")
