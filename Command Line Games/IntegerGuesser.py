from random import randint

while True:
    secret = randint(0, 4)
    guess = input("I thought of a number. Guess it:  ")
    if secret == guess:
        print ("Wow, you guessed it!")
    else:
        print ("Too bad :(. It was {}".format(secret))
