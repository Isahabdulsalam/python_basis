name1 = input("what is your name? ")
name2 = input("what is his/her name? ")

names = name1 + name2
character = names.lower()

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')

true = t + r + u + e

l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"{love_score} and you are good to go")
elif love_score >= 40 and love_score <= 50:
    print(f"{love_score} and you can be together")
else:
    print(f"{love_score}")
