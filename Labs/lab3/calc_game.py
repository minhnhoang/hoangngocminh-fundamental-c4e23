from random import randint
a = randint(0,10)
b = randint(0,10)
error = randint(-2,2)
outcome = a + b + error
print(a,"+",b,"=",outcome) #string formatting
select = input("Answer is corrent? (Y/N) ").lower()
if error == 0:
    if select == "y":
        print("Yay!")
    else:
        print("Wrong!")
else:
    if select == "y":
        print("Wrong!")
    else:
        print("Yay!")