from random import randint
x = randint(0,100)
cloud = '''
          .-~~~-.
  .- ~ ~-(       )_ _
 /                     ~ -.
|                           \
 \                         .'
   ~- . _____________ . -~
'''
print(x)
if x < 30:
    print("Rainy")
elif x < 60:
    print(cloud)
else:
    print("Sunny")
