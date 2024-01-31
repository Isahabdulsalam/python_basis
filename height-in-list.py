#write a program to calculate average height from a list of height

height = input("enter all height separate by space: ")

height_list = height.split()
count = 0

for height in height_list:
    count += 1
print(count)

for i in range(count):
    height_list[i] = int(height_list[i])

total = 0

for person in height_list:
    total += person
average = total/count

print(round(average))
