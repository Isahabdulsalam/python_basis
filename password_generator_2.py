import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbol = "$&#-+!?:'+()/,[=¥√£¶~°^¢{€"

all_character = upper + lower + number + symbol
length = int(input("How many length do u want? "))

password = ''.join(random.sample(all_character, length))
print("Generated password is :",password)
