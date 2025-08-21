import random

while True:
    secret = random.randint(1,25)
    guess_count = 0
    guess_limit = 5

    print("I'm thinking of a number between 1 and 25")

    while guess_count < guess_limit:
        guess_text = input("Take a guess: ")
        guess = int(guess_text)
        guess_count += 1

        if guess > secret:
            print(f"Too high! Try Number {guess_count}!")
        elif guess < secret:
            print(f"Too low! Try Number {guess_count}!")
        else:
            print(f"Correct! The number is {secret}!")
    
    if guess_count == guess_limit:
        cont = input(f"Game over! The correct number is {secret}! Continue? y/n?: ").lower()
    
    elif cont != "y":
        break
