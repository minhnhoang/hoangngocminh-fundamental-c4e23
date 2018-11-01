pay = [
    {
        'no': 1,
        'name': 'Huy',
        'hours': 30,
        'wage': 50,
    },
    {
        'no': 2,
        'name': 'Quan',
        'hours': 20,
        'wage': 40,
    },
    {
        'no': 3,
        'name': 'Duc',
        'hours': 15,
        'wage': 35
    }
]
print(*pay,sep='\n')
print("hours worked:")
for p in pay:
        print(p['name'],p['hours'], sep=': ')
print("salary: ")
total = 0
for p in pay:
    salary = p['hours']*p['wage']
    print(p['name'], salary, sep=': ')
    total += salary

print("total salary:", total)


