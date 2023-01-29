import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: \
            "))
        if guess < random_number:
            print("The number you guessed is too low. try again: \
                ")
        elif guess > random_number:
            print("The number you guessed is too high. try again: \
                ")
    print(f"Congrats, finally you guessed the correct number i.e. {random_number}")


guess(100)