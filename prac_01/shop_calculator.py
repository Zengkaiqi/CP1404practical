"""
sum_price = 0
DISCOUNT_INDEX = 100
DISCOUNT_RATE = 0.9
get number_of_goods
while number_of_goods < 0
    print "Invalid number"
    get number_of_goods
for i in range(1,number_of_goods+1):
    get price
    while price < 0
        print "Invalid number"
        get price
    sum_price += price
if sum_price > DISCOUNT_INDEX
    sum_price = sum_price * DISCOUNT_RATE
print number_of_goods and sum_price

"""

sum_price = 0
DISCOUNT_INDEX = 100
DISCOUNT_RATE = 0.9
number_of_goods  = int(input("How many goods do you have?"))
while number_of_goods < 0:
    print("Invalid number")
    number_of_goods = int(input("How many goods do you have?"))
for i in range(1,number_of_goods+1):
    price = float(input(f"good {i} Price:$ "))
    while price < 0:
        print("Invalid number")
        price = float(input("Price:$ "))
    sum_price += price
if sum_price > DISCOUNT_INDEX:
    sum_price = sum_price * DISCOUNT_RATE
print(f"{number_of_goods} goods need ${sum_price:.2f}")
