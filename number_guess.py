import random

number = random.randrange(11)
attempts = 0
correct = False

print("I'm thinking of a number between 1 and 10...")
tries = int(input("How many tries to guess do you want?"))
while attempts < tries and not correct:
    attempts += 1
    guess = int(input("Guess the number: "))
    if guess == number:
        correct = True
        print("Wow! You guessed right.")
    else:
        print("Hmm... Not quite.", tries - attempts, "more try.")

print("It was", number)