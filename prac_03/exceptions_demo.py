"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When user type numerator or denominator don't use the integers style
2. When will a ZeroDivisionError occur?
When user type denominator use 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
add a while loop to ask user type not 0 number
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")