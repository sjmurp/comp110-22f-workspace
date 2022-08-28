"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730549938"
    
counter = 0    
word = input("Enter a 5-character word: ")
if len(word) < 5 or len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

letter = input("Enter a single character: ")
if len(letter) > 1:
    print("Error: Character must be a single character")
    exit()
    
print("Searching for " + letter + " in " + word)

if word[0] == letter:
    print(letter + " found at index 0")
    counter+=1   

if word[1] == letter:
    print(letter + " found at index 1")
    counter+=1

if word[2] == letter:
    print(letter + " found at index 2")
    counter+=1

if word[3] == letter:
    print(letter + " found at index 3")
    counter+=1

if word[4] == letter:
    print(letter + " found at index 4")
    counter+=1

if counter > 0:
    print(str(counter) + " instances of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)

