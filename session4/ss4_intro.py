# person = ["H.Duc", "Hai Phong", "FTU", 23, 3, 257, False]

# person = {}
# print(person)
# print(type(person))

# person = {
#     "Name": "H. Duc"
# }

# print(person)
# print(type(person))

person = {
    "name": "H. Duc",
    "location": "Hai Phong",
    "age": 23
}
# print(person)

#Create
# person["friend_count"] = 257
# print(person)

#Update
# person["age"] = 24
# print(person)

#Read
# key = "school"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

#delete
del person["age"]
print(person)