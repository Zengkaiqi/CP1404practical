"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def amin():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            transfer_temperature(choice)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = transfer_temperature(choice)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

def transfer_temperature(choice):
    number_of_temperatures = float(input("Celsius: "))
    if choice == "C":
        fahrenheit = number_of_temperatures * 9.0 / 5 + 32
        return fahrenheit
    celsius = 5 / 9 * (number_of_temperatures - 32)
    return  celsius


print("Thank you.")
