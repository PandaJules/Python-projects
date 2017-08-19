import sys
from random import randint
play = True
while play:
    secret = randint(0, 4)
    guess = input("I thought of a number. Guess it:  ")
    if secret == guess:
        print ("Wow, you guessed it!")
    else:
        print ("Too bad :(. It was {}".format(secret))
        answer = input("Would you like to play again?(Enter 'y' for yes; 'n' for no): ")
        if answer == 'n':
            print("Thanks for playing.")
            input("Press Enter to exit.")
            play = False
sys.exit(0)
