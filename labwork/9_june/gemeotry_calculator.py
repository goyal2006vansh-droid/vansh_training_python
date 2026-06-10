import math

# Circle
def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

# Square
def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

# Rectangle
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

print("--------------------------------------------------------------------------------------")
from geometry import *

def get_positive_number(msg):
    while True:
        try:
            num = float(input(msg))
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        except:
            print("Invalid input.")

while True:
    print("\n===== Figure Menu =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    figure = input("Enter your choice: ")

    if figure == "4":
        print("Thank you for using the application!")
        break

    elif figure == "1":
        radius = get_positive_number("Enter radius: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter your choice: ")

            if op == "1":
                print("Area of Circle =", round(circle_area(radius), 2))
            elif op == "2":
                print("Perimeter of Circle =", round(circle_perimeter(radius), 2))
            elif op == "3":
                break
            else:
                print("Invalid choice.")

            ch = input("Perform another operation on same figure? (Y/N): ")
            if ch.upper() != "Y":
                break

    elif figure == "2":
        side = get_positive_number("Enter side: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter your choice: ")

            if op == "1":
                print("Area of Square =", square_area(side))
            elif op == "2":
                print("Perimeter of Square =", square_perimeter(side))
            elif op == "3":
                break
            else:
                print("Invalid choice.")

            ch = input("Perform another operation on same figure? (Y/N): ")
            if ch.upper() != "Y":
                break

    elif figure == "3":
        length = get_positive_number("Enter length: ")
        breadth = get_positive_number("Enter breadth: ")

        while True:
            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = input("Enter your choice: ")

            if op == "1":
                print("Area of Rectangle =", rectangle_area(length, breadth))
            elif op == "2":
                print("Perimeter of Rectangle =", rectangle_perimeter(length, breadth))
            elif op == "3":
                break
            else:
                print("Invalid choice.")

            ch = input("Perform another operation on same figure? (Y/N): ")
            if ch.upper() != "Y":
                break

    else:
        print("Invalid figure choice.")

    cont = input("\nDo you want to continue using the application? (Y/N): ")
    if cont.upper() != "Y":
        print("Thank you for using the application!")
        break
