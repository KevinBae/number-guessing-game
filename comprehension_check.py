import random

secret = random.randint(1,50)
print("I'm thinking of a number between 1 and 50:")

guesses = 0

while True:
    guess_text = input("Take a guess: ")
    guess = int(guess_text)
    guesses += 1

    if guesses == 5:
        print("Try number", guesses, "!","Too many guesses!")
        break
    elif guess > secret:
        print("Too high! Try number", guesses, "!")
    elif guess < secret:
        print("Too low! Try number", guesses, "!")
    else:
        print("You got it! The number was", secret)
        break

