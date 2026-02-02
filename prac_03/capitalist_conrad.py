import random
MAX_STOCK_PRICE = 1000
MIN_STOCK_PRICE = 0.01
PERCENTAGE_OF_INDEX = 50
FILENAME = "stock_prices.txt"
number_of_days = 1
stock_price = 10
percentage_chance = random.randint(1, 100)

out_file = open(FILENAME, "w")
while MIN_STOCK_PRICE < stock_price < MAX_STOCK_PRICE:
    if percentage_chance <= PERCENTAGE_OF_INDEX:
        daily_change = random.uniform(0,0.1)
    else:
        daily_change = -random.uniform(0,0.05)
    stock_price = stock_price + daily_change *stock_price
    print(f"day {number_of_days} price is ${stock_price:.2f}", file=out_file)
    number_of_days += 1
out_file.close()

