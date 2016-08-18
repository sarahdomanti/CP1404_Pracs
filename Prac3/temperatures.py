"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Sarah'

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

while choice != "Q":
    if choice == "C":
        fahrenheit = celsius_to_fahrenheit(float(input("Celsius: ")))
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        celsius = fahrenheit_to_celsius(float(input("Fahrenheit:  ")))
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
