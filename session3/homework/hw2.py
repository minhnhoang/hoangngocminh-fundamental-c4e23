print("Hi there, this is a superuser gateway")
username = input("Username: ")
while username != "c4e":
    print("You are not superuser")
    username = input("Username: ")
password = input("Password: ")
while password != "codethechange":
    print("Password is incorrect")
    password = input("Password: ")
print("Welcome, c4e")