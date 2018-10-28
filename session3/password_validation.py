pw = input("Enter password: ")

while True:
    if len(pw) <= 8:
        print("Password length must be greater than 8")
    elif pw.isalpha():
        print("Password must contain number")
    elif pw.isupper() or pw.islower():
        print("Password must contain both lower and upper case")
    elif pw.isdigit():
        print("Password must contain character")
    else:
        break
    pw = input("Enter password: ")