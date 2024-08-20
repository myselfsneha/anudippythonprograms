import random

# Generate a random number between 0 and 20
magic_number = random.randint(0, 20)

guess = None

while guess != magic_number:
    guess = int(input("Guess a number between 0 and 20: "))
    if guess == magic_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Incorrect guess. Try again.")
