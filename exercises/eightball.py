from random import randint

question: str = input("Ask a yes/no question...")
response: int = randint(0, 2)

if response == 0:
    print("yes, definitely")
else:
    if response == 1:
        print("Ask again later")
    else:
        print("no bueno")

