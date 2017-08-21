import sys
from random import randint
play = True
while play:
    secret = randint(1, 5)
    guess = input("I thought of a number from 1 to 5. Guess it:  ")
    if str(secret) == guess:
        print("Wow, you guessed it!")
    else:
        print("Too bad :(. It was {}".format(secret))
        answer = input("Would you like to play again?(Enter 'y' for yes; 'n' for no): ")
        if answer == 'n':
            print("Thanks for playing.")
            input("Press Enter to exit.")
            play = False
sys.exit(0)
