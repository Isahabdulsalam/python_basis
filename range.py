#Calculate the sum of even number from 0 to 1 include 0 and 100

total = 0

for i in range(1,101):
    if i % 2 == 0:
        total += i
print(total)
