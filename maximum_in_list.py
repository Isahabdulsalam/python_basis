#find the maximun number in the list

numbers = input("Enter list of number separate by space: ")

#12 54 67 87 -60

numbers_list = numbers.split()
count = 0

for number in numbers_list:
    count += 1
print(f"The length of the number is : {count}")

for i in range(count): #0 1 2 3 4 5
    numbers_list[i] = int(numbers_list[i])
maximum_number = numbers_list[0]

for number in numbers_list:
    if number > maximum_number:
        maximum_number = number
print(f"The maximum number is: {maximum_number}")
