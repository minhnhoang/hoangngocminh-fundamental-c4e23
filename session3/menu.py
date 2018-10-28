# item1 = "Phở xào"
# item2 = "Ghẹ"
# item3 = "Sò huyết"
# item4 = "Cháo"
# item5 = "Cơm rang"

# items = [] # Empty list
# print(items)
# print(type(items))

items =["Ghẹ", "So huyet", "Chao"]
print(items)
i = int(input("Index: "))
new_value = input("New value: ")
items[i] = new_value
print(items)

# items.pop(1) #delete by position
# print(items)

items.remove("So huyet") #delete by content
print(items)