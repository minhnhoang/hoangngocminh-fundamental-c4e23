sheeps = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Minh and these are my sheep sizes:", sheeps, sep='\n')

for m in range(3):
    biggest = max(sheeps)
    print("Now my biggest sheep has size", biggest,"let's shear it!")
    sheeps[sheeps.index(biggest)] = 8
    print("After shearing, hear is my flock: ",sheeps, sep='\n')
    print("Month",m+1)
    for i in range(len(sheeps)):
        sheeps[i] = sheeps[i] + 50
    print("One month has passed, now here is my flock:", sheeps, sep='\n')

size = sum(sheeps)
print("My flock has size in total:", size)
print("I would get",size,"* $2 = $", size*2)