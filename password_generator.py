import random

# Your existing lists of characters
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '$', '&', '@', '(', ')', ':', '/', '#', '+']

print("Welcome to the password generator!")

ltrs = int(input("How many letters do you want?\n"))
num = int(input("How many numbers do you want?\n"))
sym = int(input("How many symbols do you want?\n"))
password_list = []

for i in range(1, ltrs + 1):
    character = random.choice(letters)
    password_list += character
for i in range(1, num + 1):
    number = random.choice(numbers)
    password_list += number
for i in range(1, sym + 1):
    symbol = random.choice(symbols)
    password_list += symbol
password = ""
random.shuffle(password_list)
for char in password_list:
    password += char
print(password)

