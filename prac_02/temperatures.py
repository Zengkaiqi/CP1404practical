"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temperature = transfer_temperature(choice,"Celsius: ")
            union = "F"
        elif choice == "F":
            temperature = transfer_temperature(choice,"Fahrenheit: ")
            union = "C"
        else:
            print("Invalid option")
        print(f"Result: {temperature:.2f} {union}")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def transfer_temperature(choice,prompt):
    number_of_temperatures = float(input(prompt))
    if choice == "C":
        fahrenheit = number_of_temperatures * 9.0 / 5 + 32
        return fahrenheit
    celsius = 5 / 9 * (number_of_temperatures - 32)
    return  celsius


main()