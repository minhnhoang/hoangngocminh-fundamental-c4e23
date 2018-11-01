correct = 0
print("Answer the following algebra question:", "If x=8 then what is the value of 4(x+3) ?", sep='\n')
choices = {
    1: 35,
    2: 36,
    3: 40,
    4: 44,
}
for i in choices.keys():
    print(i,choices[i], sep='. ')
selection = int(input("Your choice:" ))
if choices[selection] == 4 *(8+3):
    print("Bingo!")
    correct += 1
else:
    print(":(")

print("Estimate this answer (exact calculation not needed):", "Jack scored these marks in 5 math tests: 49, 81, 72, 66, and 52. What is the mean?", sep='\n')
choices = {
    1: "About 55",
    2: "About 65",
    3: "About 75",
    4: "About 85",
}
for i in choices.keys():
    print(i,choices[i], sep='. ')
selection = int(input("Your choice:" ))
if selection == 2:
    print("Bingo!")
    correct += 1
else:
    print(":(")
print("You correctly answer", correct, "out of 2 questions")
