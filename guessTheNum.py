#Guess the random number

import random
print("Hello! Let's play!")
guesses = 6
number = random.randint(1, 100)
win = False

while guesses > 0:
    guess = int(input("Guess: "))

    if guess > number:
        print("your guess was too high, you have", guesses, "remaining")
    elif guess < number:
        print("your guess was too low, you have", guesses, "remaining")
    else:
        print("NICE GUESS!")
        win = True
        guesses = 0
    guesses -= 1

if win == False:
    print("I'm sorry the number was", number)
