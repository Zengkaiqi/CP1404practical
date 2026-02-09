import random
numbers = []
number_of_line = int(input("How many quick picks?"))
for i in range(number_of_line):
    for j in range(6):
        random_number = random.randint(1, 45)
        numbers.append(random_number)
        numbers.sort()
    for number in numbers:
        print(f"{number:>4}", end=" ")
    numbers = []
    print()