from turtle import *
for sides in range (3,7):
    if sides%2 == 0:
        color('red')
    else:
        color('blue')
    for s in range(sides):
        angle = 360/sides
        forward(100)
        left(angle)
mainloop()