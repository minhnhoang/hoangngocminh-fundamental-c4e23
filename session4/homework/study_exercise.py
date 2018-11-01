letter_counts = {}
sentence = input("Request sentence: ").lower().replace(" ","")
for letter in sentence:
    letter_counts[letter] = letter_counts.get(letter,0) + 1

letter_items = list(letter_counts.items())
letter_items.sort()
print(*letter_items,sep='\n')

