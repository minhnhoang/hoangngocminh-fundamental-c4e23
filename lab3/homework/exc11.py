def is_inside(point,rectangle):
    a1 = rectangle[0]
    b1 = rectangle[1]
    a2 = rectangle[0] + rectangle[2]
    b2 = rectangle[1] + rectangle[3]
    if (a1 <= point[0] <= a2) and (b1 <= point[1] <= b2):
        print("True")
    else:
        print("False")

is_inside([100,120],[140,60,100,200])
is_inside([200, 120], [140, 60, 100, 200])