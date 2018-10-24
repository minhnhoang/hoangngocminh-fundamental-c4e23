a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b*b - 4*a*c
a2 = 2*a
if a == 0:
    print("x =",-c/b)
elif delta < 0:
    print("No solution")
elif delta == 0:
    x = -b/a2
    print("1 solution x =",x)
else:
    delta_sqrt = -b + delta**0.5
    x1 = delta_sqrt/a2
    x2 = delta_sqrt/a2
    print("2 solutions: ", x1, x2)