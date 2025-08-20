import random

secret = random.randint(1,20)
print("I am thinking of a number between 1 and 20...")

while True:
    guess_text = input("Take a guess: ")
    guess = int(guess_text)

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it! The number was", secret)
        break