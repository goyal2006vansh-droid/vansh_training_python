charging_level = 20
while charging_level <= 100:
    if electricity_status:
        print("battery level is", charging_level, "%")
        charging_level = charging_level + 10
    else:
        break

print("full charge")
