from random import randint, choice
from calc import eval

def gen_quiz():
    o = choice(["+","-","*","/"])
    x = randint(0,10)
    y = randint(0,10)
    error = choice([-1,1,-2,2,0,0,0])
    r = eval(x,y,o) + error
    return x,y,o,r

a,b,op,r = gen_quiz()
print(a,op,b,"=",r)
select = input("Answer is corrent? (Y/N) ").lower()
if r == eval(a,b,op):
    if select == "y":
        print("Yay!")
    else:
        print("Wrong!")
else:
    if select == "y":
        print("Wrong!")
    else:
        print("Yay!")