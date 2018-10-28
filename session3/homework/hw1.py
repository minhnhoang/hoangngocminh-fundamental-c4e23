print("Hi there, this is a superuser gateway")
username = input("Username: ")
if username != "c4e":
    print("You are not superuser")
else:
    password = input("Password: ")
    if password != "codethechange":
        print("Password is incorrect")
    else:
        print("Welcome, c4e")