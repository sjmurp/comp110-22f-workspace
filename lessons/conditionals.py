"""An example of conditional if-else statements"""

SECRET: int = 3

print("Im thinking of a value between 1 and 5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!")
    print("Have a good time")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("Guess high")
    else:
        print("Guess too low")

print("Game Over.")
