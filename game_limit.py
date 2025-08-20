import random

secret = random.randint(1,50)
print("I'm thinking of a number between 1 and 50:")

guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    guess_text = input("Take a guess: ")
    guess = int(guess_text)
    guess_count += 1

    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print("You got it! The number is", secret)
        break

if guess_count == guess_limit:
    print("Out of guesses! The number was", secret)