items = ["T-shirt", "Sweater"]

choice = input("Welcome to our shop, what do you want (C, R, U, D)? ")

while choice in ["C","c","R","r","U","u","D","d"]:
    if choice == "C" or choice == "c":
        new = input("Enter new item: ")
        items.append(new)

    elif choice == "U" or choice == "u":
        position = int(input("Update position: "))
        while position > len(items):
            print("Position out of range, please select position upto", len(items))
            position = int(input("Update position: "))
        update = input("New item: ")
        items[position-1] = update

    elif choice == "D" or choice == "d":
        delete = int(input("Delete position: "))
        while delete > len(items):
            print("Position out of range, please select position upto", len(items))
            position = int(input("Update position: "))
        items.pop(delete-1)

    print("Our items:", end=' ')
    print(*items, sep=', ')
    choice = input("Welcome to our shop, what do you want (C, R, U, D)? ")