"""Wordle game, but only one guess."""

__author__ = "730549938"

s_word: str = "python"
guess: str = ""
guess = input("What is your 6-letter guess? ")
index_counter: int = 0
winner_count: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(s_word):
    guess = input("That was not 6 letters! Try again: ")

while index_counter < len(s_word):
    if s_word.find(guess[index_counter]) < 0:
        print(WHITE_BOX, end = ' ')
    if s_word.find(guess[index_counter]) >= 0:
        if guess[index_counter] == s_word[index_counter]:
            print(GREEN_BOX, end = ' ')
            winner_count += 1
        else:
            print(YELLOW_BOX, end = ' ')
    index_counter+= 1
if winner_count == 6:
    print("\nWoo! You got it!")
else:
    print("\nNot quite. Play again soon!")