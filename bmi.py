weight = input("What is your weight in KG? ")
height = input("What is your weight in KG? ")

bmi = int(weight)/float(height)*2
if bmi < 16.0:
    print("you are underweight severe thinness")
elif bmi < 17.0:
    print("you are underweight moderate thinness")
elif bmi > 18.5:
    print("you are normal")
elif bmi > 25.0:
    print("you are obese (class i)")
elif bmi > 30.0:
    print("you are obese (class ii)")
elif bmi > 35.0:
    print("you are obese (class iii)")
else:
    print("not define")
#print("Your Body Mass is " + str(round(bmi, 2)))
