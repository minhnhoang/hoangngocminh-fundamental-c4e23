s = input("Enter a text: ")
print(s.isupper())
print(s.islower())
print(s.isalpha())
print(s.isdigit())
if (not s.isdigit()) and (not s.islower()) and (not s.isupper()):
    print("Contains both lower and uppercase")
else:
    print("Not OK")