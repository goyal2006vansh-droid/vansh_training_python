# Vehicle Registration Analyzer

vehicles = [
    "MH12AB4589", "MH14CD1234", "MH20EF5678", "MH01GH9876", "MH10IJ3456",
    "MH22KL1111", "DL05XY9988", "DL01AB1234", "DL10CD5678", "DL07EF4321",
    "KA03PQ1234", "KA05RS5678", "KA09TU9876", "KA11VW2345", "KA15XY6789",
    "UP12AB1111", "UP14CD2222", "UP16EF3333", "UP18GH4444", "UP20IJ5555"
]

state_count = {}
invalid = []

for reg in vehicles:

    print("\nRegistration Number:", reg)

    # Validate format
    valid = (
        len(reg) == 10 and
        reg[:2].isalpha() and
        reg[2:4].isdigit() and
        reg[4:6].isalpha() and
        reg[6:].isdigit()
    )

    if not valid:
        invalid.append(reg)
        print("Invalid Registration")
        continue

    # Extract details
    state = reg[:2]
    district = reg[2:4]
    series = reg[4:6]
    vehicle_no = reg[6:]

    # Count letters and digits
    letters = 0
    digits = 0

    for ch in reg:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1

    print("State Code   :", state)
    print("District Code:", district)
    print("Series       :", series)
    print("Vehicle No   :", vehicle_no)
    print("Letters      :", letters)
    print("Digits       :", digits)

    # State-wise count
    if state in state_count:
        state_count[state] += 1
    else:
        state_count[state] = 1

# Invalid registrations
print("\n===== INVALID REGISTRATIONS =====")
for reg in invalid:
    print(reg)

# State-wise report
print("\n===== STATE-WISE REPORT =====")
for state in state_count:
    print(state, "->", state_count[state], "Vehicles")
