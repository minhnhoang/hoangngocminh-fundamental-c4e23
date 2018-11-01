items = ["chao", "mien", "pho"]
number = ["I", "II", "III"]
no = 1
for i in items:
    # print(items.index(i)+1,i, sep=". ")
    print(no, i)
    no += 1

for i in items:
    print(number[items.index(i)], i, sep=". ")