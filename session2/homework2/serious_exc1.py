height = int(input("Your heith (cm): "))
m = int(input("Your weight (kg): "))
h = height/100
bmi = round(m / (h*h),1)
print("Your BMI:", bmi)
if bmi < 16:
    print("You are severely underweight!")
elif bmi < 18.5:
    print("You are underweight!")
elif bmi < 25:
    print("You are of normal weight!")
elif bmi < 30:
    print("You are overweight!")
else:
    print("You are obese!")