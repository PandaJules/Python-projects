from random_words import RandomWords
import sys


def play():
    secret_word = RandomWords().random_word()
    tries = 10
    print("I came up with a word. Try to guess it!")
    print("You have {} attempts left".format(tries))
    reveal('', secret_word)
    guessed_so_far = []
    tried_so_far=[]
    guessed_the_word = False
    while tries > 0 and not guessed_the_word:
        user_guess = input('Guess one letter: ')
        print("")
        if user_guess in tried_so_far:
            print("You already tried that letter.")
        else:
            tried_so_far.append(user_guess)
            if user_guess in secret_word:
                guessed_so_far.append(user_guess)
                reveal(guessed_so_far, secret_word)
                guessed_the_word = didwin(guessed_so_far, secret_word)
                if guessed_the_word:
                    print("Congratulation! The word was {}.".format(secret_word))
            else:
                tries -= 1
                failure(user_guess, tries, secret_word)
                reveal(guessed_so_far, secret_word)
    print("Would you like to play again?")
    again = input("Yes or No?   ")
    if again.lower() == 'yes':
        play()
    else:
        print ("See you next time! Bye!")


def reveal(guessed_so_far, word):
    for l in word:
        if l in guessed_so_far:
            sys.stdout.write(l+" ")
        else:
            sys.stdout.write('_ ')
    print('')


def failure(user_guess, tries, word):
    print("\t\t{} is not in the word.".format(user_guess))
    if tries == 0:
        print("\t\tYou ran out of lives. Game is over. The word was {}.".format(word))
    else:
        print("\t\tYou have {} attempts left".format(tries))
        print("")


def didwin(guessed, word):
    if sorted(guessed) == sorted(list(set(word))):
        return True
    else:
        return False

play()
