"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
HIGH_BONUS_INDEX = 1000
LOW_RATE = 0.1
HIGH_RATE = 0.15
GET sales
while sales >= 0
    if sales < HIGH_BONUS_INDEX
        rate = LOW_RATE
    else
        rate = HIGH_RATE
    print sales * rate
    get sales
"""

HIGH_BONUS_INDEX = 1000
LOW_RATE = 0.1
HIGH_RATE = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < HIGH_BONUS_INDEX:
        rate = LOW_RATE
    else:
        rate = HIGH_RATE
    print(f"Bonus is {sales * rate}")
    sales = float(input("Enter sales: $"))


