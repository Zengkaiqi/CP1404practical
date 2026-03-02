out_file = open("name.txt", "w")
user_name = input("Enter your name: ")
out_file.write(user_name)
out_file.close()
in_file = open("name.txt", "r")
name = in_file.readline()
print("HI",name,"!")
in_file.close()
create_file = open("numbers.txt", "w")
print(17,file=create_file)
print(42,file=create_file)
print(400,file=create_file)
create_file.close()
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number =int(file.readline())
result = first_number + second_number
print(result)
sum_number = 0
with open("numbers.txt", "r") as file:
    for line in file:
        sum_number += int(line)
    print(sum_number)