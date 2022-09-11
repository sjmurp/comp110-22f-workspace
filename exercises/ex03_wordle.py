"""Wordle game."""

__author__ = "730549938"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, letter: str) -> bool:
    """This checks if the letter is in the string"""
    index: int = 0
    assert len(letter) == 1
    while index < len(word):
        if word[index] == letter:
            return True
        index += 1
    return False

def emojified(ans: str, guess: str) -> str:
    """This makes the emoji representation of the guess."""
    #assert len(ans) == len(guess)
    index: int = 0
    result: str = ""
    while index < len(guess):
        if guess[index] == ans[index]:
            """This checks whether the letter is in the string and in the correct spot"""
            result += GREEN_BOX
        elif contains_char(ans, guess[index]):
            result += YELLOW_BOX   
        else:
            result += WHITE_BOX
        index += 1
    return result

def input_guess(length: int) -> str:
    """This checks to see if guess is correct length"""
    user_ans = input(f"Enter a {length} character word: ")
    while len(user_ans) != length:
        user_ans = input(f"That wasn't {length} chars! Try again: ")
    return user_ans
    
    
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"
    while turn <= 6:
        guessed: str = input_guess(len(secret))
        print(f"=== Turn {turn}/6 ===")

        print(emojified(secret, guessed))
        if secret == guessed:
            print(f"You won in {turn} turns!")
            return
        else:
            turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()

