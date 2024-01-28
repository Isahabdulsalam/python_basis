import random

name = input("Enter everyone name to selecting the one that will pay the bill separeted by comma: ")

name_list = name.split(",") #separate the names

length = len(name_list)
random_choice = random.randint(0, length-1)
print(f"{name_list[random_choice]} will pay the bill")
