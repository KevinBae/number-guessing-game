import random

secret = random.randint(1,50)
print("I'm thinking of a number between 1 and 50:")

guess_count = 0
guess_limit = 5

while True:
    continue = input("Type 'quit' to stop, anything else to quit: ")