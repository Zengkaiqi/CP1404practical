numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])       #answer : 3
print(numbers[-1])      #answer : 2
print(numbers[3])       #answer : 5
print(numbers[:-1])     #answer : [3,1,4,1,5,9]
print(numbers[3:4])     #answer : [1]
print(5 in numbers)     #answer :  True
print(7 in numbers)     #answer :  False
print("3" in numbers)   #answer :  False
print(numbers + [6, 5, 3])  #answer : [3,1,4,1,5,9,2,6,5,3]


#1 Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

#2 Change the last element of numbers to 1
numbers[-1] = 1

#3 Print all the elements from numbers except the first two (slice)
print(numbers[2:])

#4 Print whether 9 is an element of numbers
print(9 in numbers) 