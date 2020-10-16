import random

def play_guess_the_number()
    minVal = int(input("Minimum?\n"))
    maxVal = int(input("Maximum?\n"))
    number = random.randrange(minVal, maxVal, 1)

    runState = True
    guess = int(input(f"I am thinking of a number between {minVal} and {maxVal}.  Can you guess what it is?"))
    while (runState):
        if (guess < number):
            guess = int(input("Too low, Try again: "))
        if (guess > number):
            guess = int(input("Too high, Try again: "))
        if (guess == number):
            runState = False
            print("Congratulations! You guessed my number!")

play_guess_the_number()