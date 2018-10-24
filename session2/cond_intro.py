yob = int(input("Year of birth: "))
age = 2018 - yob
print("Your age:",age)

if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
elif age < 21:
    print("Junior")
else:
    print("Adult")

print("Bye!")