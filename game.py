import random

round_count = 0
win_count = 0
loss_count = 0

while True:
    secret = random.randint(1,25)
    guess_count = 0
    guess_limit = 5
    round_count += 1

    print(f"Round {round_count}")
    print("I'm thinking of a number between 1 and 25")

    while guess_count < guess_limit:
        guess_text = input("Take a guess: ")
        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a number. That didn’t count as an attempt.")
        continue

        guess_count += 1

        if guess > secret:
            print(f"Too high! Attempt {guess_count} of {guess_limit}!")
        elif guess < secret:
            print(f"Too low! Attempt {guess_count} of {guess_limit}!")
        else:
            win_count += 1
            print(f"Correct! The number is {secret}!")
            break
    
    if guess_count == guess_limit:
        loss_count += 1
        print(f"Game over! The correct number is {secret}!")
        
    print(f"Wins: {win_count} | Losses: {loss_count}")
        
    again = input("Continue? y/n: ").strip().lower()
    
    if again != "y":
        print(f"Wins: {win_count} | Losses: {loss_count}")
        print(f"Thanks for playing!")
        break