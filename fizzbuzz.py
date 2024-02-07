#Fizzbuzz job interview question

"""
if - the number is divisible by 3 print "Fizz"
if - the number is divisible by 5 print "Buzz"
if - the number is divisible by 3 and 5 print "FizzBuzz"
else - none
"""

for i in range(1,101):
    if i % 3 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
