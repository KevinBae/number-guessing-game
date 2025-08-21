import random

while True:
    secret = random.randint(1,50)
    guess_count = 0
    guess_limit = 5

    print("I am thinking of a number between 1 and 50...")

    while guess_count < guess_limit:
        guess_text =input("Take a guess: ")
        guess = int(guess_text)
        guess_count += 1

        if guess > secret:
            print(f"Too high! Try number {guess_count}!")
        elif guess < secret:
            print(f"Too low! Try number {guess_count}!")
        else:
            print(f"That is correct! The number was {secret}. It took you {guess_count} tries!")
            break
    
    if guess_count == guess_limit:
        print(f"Sorry, you're out of guess. The number was {secret}!")

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
