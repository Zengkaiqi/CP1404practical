numbers = []
for i in range(5):
    element = int(input("input number: "))
    numbers.append(element)
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The minimum number is", min(numbers))
print("The maximum number is", max(numbers))
print("The average number is", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input("enter your name: ")
if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")
