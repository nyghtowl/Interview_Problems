import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else: 
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_so_far = list(len(secretWord) * '_')

    for i, letter in enumerate(secretWord):
        if letter in lettersGuessed:
            guessed_so_far[i] = letter
    return ''.join(guessed_so_far)

def getGuessedWord_alt(secretWord, lettersGuessed):
    answer = []
    for i in secretWord:
        if i in lettersGuessed:
            answer.append(i + ' ')
        else:
            answer.append('_ ')
    return ''.join(answer)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        result.remove(letter)
    return ''.join(result)


if __name__ == '__main__':
    # Test Cases
    print("trying isWordGuessed")
    print("isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']) == False: %s") % (isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']) == False)
    print("isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']) == True: %s") % (isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']) == True)
    print("isWordGuessed('pineapple', ['q', 'v', 's', 'k', 'e', 'o', 'r', 't', 'h', 'n']) == False: %s") % (isWordGuessed('pineapple', ['q', 'v', 's', 'k', 'e', 'o', 'r', 't', 'h', 'n']) == False)
    isWordGuessed('coconut', []) == False
    isWordGuessed('carrot', ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't']) == True

    print("trying getGuessedWord")
    print("getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']) == '_pp_e': %s ") % (getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']) == '_pp_e')
    getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']) == 'durian'
    getGuessedWord('broccoli', ['f', 'c', 'q', 'b', 'z', 'p', 't', 'u', 'g', 'a']) == 'b__cc___'
    getGuessedWord('grapefruit', []) == '__________'

    print("trying getAvailableLetters")
    print("getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']) == 'abcdfghjlmnoqtuvwxyz': %s") % (getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']) == 'abcdfghjlmnoqtuvwxyz')
    getAvailableLetters([]) == 'abcdefghijklmnopqrstuvwxyz'
    getAvailableLetters(['e', 'p', 'v', 'f', 's', 'q', 'n', 'h', 'b', 'z', 'l', 'r']) == 'acdgijkmotuwxy'
    getAvailableLetters(['y', 'g', 'w', 'c', 'u', 'z', 'l', 'q', 't']) == 'abdefhijkmnoprsvx'