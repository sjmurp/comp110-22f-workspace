"""Wordle game, but only one guess."""

__author__ = "730549938"

s_word: str = "python"
guess: str = ""
guess = input("What is your 6-letter guess? ")
index_counter: int = 0
alt_index: int = 0
winner_count: int = 0
existence: bool = False
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(s_word):
    guess = input("That was not 6 letters! Try again: ")

while index_counter < len(guess):
    if guess[index_counter] == s_word[index_counter]:
            """This checks whether the letter is in the string and in the correct spot"""
            print(GREEN_BOX, end = ' ')
            winner_count += 1
    else:
        while existence == False and alt_index < len(s_word):
            """This checks if the letter is at least in the string"""
            if guess[index_counter] == s_word[alt_index]:
                existence = True
            else:
                alt_index += 1
        if existence == True:
            print(YELLOW_BOX, end = ' ')
        else:
            print(WHITE_BOX, end = ' ')

    index_counter += 1

if winner_count == 6:
    print("\nWoo! You got it!")
else:
    print("\nNot quite. Play again soon!")
