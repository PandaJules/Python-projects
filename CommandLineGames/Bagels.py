import random


def get_digits():
    # Get the number of digits for the secret number
    print("Let's play BAGELS!")
    while True:
        num_digits = int(input("How many digits do you want in your number?   "))
        if 0 < num_digits < 10:
            return num_digits
        else:
            print("Please give a number of digits 1-5")
            print("")


def introduction(num_digits):
    # Introduce the rules
    print('\nI came up with a {}-digit number. Guess it.'.format(num_digits))
    print('Here are some clues:')
    print('When I say:    That means:')
    print('  Pico         One digit is correct but in the wrong position.')
    print('  Fermi        One digit is correct and in the right position.')
    print('  Bagels       No digit is correct.')


def print_clues(user_guess, secret_number):
    # Analyse digits of the guessed number and print Fermi/Pico/Bagels
    if user_guess == secret_number:
        print("You won! That's what I guessed")
    else:
        clue = ""
        for i in range(len(user_guess)):
            if user_guess[i] == secret_number[i]:
                clue += "Fermi"
            elif user_guess[i] in secret_number:
                clue += "Pico"
        if len(clue) == 0:
            print("Bagels")
        else:
            print(clue)


def play(num_digits):
    range_start = 10 ** (num_digits - 1)
    range_end = (10 ** num_digits) - 1
    secret_number = random.randint(range_start, range_end)
    while True:
        user_guess = ''
        while len(user_guess) != num_digits:
            user_guess = input('Your guess: ')

        # Arguments are arrays of integers that are digits of user_guess and secret_number
            print_clues([int(d1) for d1 in str(user_guess)], [int(d2) for d2 in str(secret_number)])

        if int(user_guess) == secret_number:
            break


def play_again_prompt():
    print("Would you like to play again?")
    if input().lower().startswith('y'):
        start()


def start():
    num_digits = get_digits()
    introduction(num_digits)
    play(num_digits)
    play_again_prompt()


start()
