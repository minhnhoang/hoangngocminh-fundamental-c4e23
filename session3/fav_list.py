fav_list = ["trekking", "travelling", "reading"]

print("Hi there, here are your favorite things so far")
for i in range(3):
    print(i+1, fav_list[i])

a = int(input("Position you want to update? "))
a_value = input("Your new favorite thing? ")
# fav_list.append(add) =>> add to end of list

fav_list[a] = a_value
print(*fav_list, sep='\n')

d = int(input("Position you want to delete? "))
fav_list.pop(d)
print(*fav_list, sep='\n')