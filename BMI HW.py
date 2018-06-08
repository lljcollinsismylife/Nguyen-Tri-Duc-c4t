height = int(input("enter your height in Cm:"))
weight = int(input("enter your weight in Kg:"))

convertedheight = (height / 100) ** 2
BMI = weight / convertedheight

print("Your BMI:", BMI)
if BMI < 16:
    print("You are severely underweight")
elif BMI < 18.5:
    print(" you are under weight")
elif BMI < 25:
    print(" You are normal")
elif BMI < 30:
    print(" You are overweight")
else:
    print(" Sadly you are obese")
