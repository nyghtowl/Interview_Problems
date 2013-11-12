# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
from hangman_helper import getAvailableLetters, isWordGuessed, getGuessedWord

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    num_guesses = 8
    lettersGuessed = []
    won = False

    print("Welcome to the game, Hangman! \nI am thinking of a word that is %d letters long.") % len(secretWord)

    while num_guesses > 0:
        print("-----------")
        print("You have %d guesses left") % num_guesses
        print("Available Letters: %s") % getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter:")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: %s") % remaining
            continue
        lettersGuessed.append(guess)
        remaining = getGuessedWord(secretWord, lettersGuessed)
        if guess in secretWord:
            print("Good guess: %s") % remaining
        else:
            num_guesses -= 1
            print("Oops! That letter is not in my word: %s") % remaining


        if isWordGuessed(secretWord, lettersGuessed):
            print("-----------")
            print("Congratulations, you won!")
            won = True
            break
        
    if not won:
        print("-----------")
        print("Sorry, you ran out of guesses. The word was %s.") % secretWord





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)