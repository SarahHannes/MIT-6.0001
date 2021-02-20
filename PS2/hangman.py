# Problem Set 2, hangman.py
# Name: Sarah Hannes
# Collaborators: None 😎
# Start Time: 9/12/2020 1:54PM
# End Time: 9/12/2020 10:33PM
# Time spent: 08:39:00

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter in letters_guessed:
            result = True
        else:
            return False
    return result


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = []
    for letter in secret_word:
        if letter in letters_guessed:
            result.append(letter)
        else:
            result.append('_ ')
    return ''.join(result)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in all:
            all = all.replace(letter, '')
    return all
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    initial_guess = 6
    guess = initial_guess
    initial_warning = 3
    warning = initial_warning
    letters_guessed = []
    vowels = 'aeiou'
    unique_letters = ''.join(set(secret_word))  # stores only the unique letters in secret word

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warning} warnings left.')
    print('----------------')

    while guess > 0:
        print(f'You have {guess} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guessed_letter = input('Please guess a letter:').lower()
        if not guessed_letter.isalpha():  # if user's input is not an alphabet
            if warning != 0:
                warning -= 1
                print(f'Oops! That is not a valid letter. You have {warning} warnings left. {get_guessed_word(secret_word, letters_guessed)}')
            else:
                guess -= 1
                print(f"Oops! That is not a valid letter. You have no warning left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
            print('----------------')

        else:  # if user's input is an alphabet
            if guessed_letter in letters_guessed:  # if user has already guessed the letter
                if warning != 0:
                    warning -= 1
                    print(f"Oops! You've already guessed that letter. You have {warning} warning left: {get_guessed_word(secret_word, letters_guessed)}")
                else:
                    guess -= 1
                    print(f"Oops! You've already guessed that letter. You have no warning left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                print('----------------')
            if guessed_letter not in letters_guessed:  # if the user had not already guessed the letter
                letters_guessed.append(guessed_letter)
                if guessed_letter in secret_word:  # if the guessed letter is in secret word
                    print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
                else:  # if the guessed letter is not in secret word
                    if guessed_letter in vowels:  # if the guessed word is a vowel
                        guess -= 2
                    else:  # if the guessed word is not a vowel
                        guess -= 1
                    print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
                print('----------------')
            if is_word_guessed(secret_word, letters_guessed):  # if the secret word has been guessed
                print(f'Congratulations, you won!')
                print(f'Your total score for this game is: {guess * len(unique_letters)}')
                break
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.strip(' ')  # strip spaces before and after the word
    my_word = my_word.replace(' ', '')  # remove all spaces in the word
    other_word = other_word.strip(' ')  # strip spaces before and after the word
    if len(my_word) == len(other_word):
        for n in range(len(my_word)):
            if my_word[n] != '_':  # if the letter is not '_'
                if my_word[n] == other_word[n]:  # check if the letter is equal to the letter in other_word in the same position
                    result = True
                else:
                    return False
            elif my_word[n] == '_':  # if the letter is '_'
                if other_word[n] in my_word:  # check if the letter in other_word at the same position as '_' is already in my_word
                    return False  # if it is return False
                continue  # if it is not, continue looking at the next letter in sequence
        return result  # when all letters in my_word had been iterated, return result
    return False  # if len(my_word) != len(other_word), return false


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.strip(' ')  # strip spaces before and after the word
    my_word = my_word.replace(' ', '')  # remove all spaces in the word
    matched = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched.append(word)
        else:
            continue
    if len(matched) == 0:
        print('No matches found')
    else:
        print(' '.join(matched))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    initial_guess = 6
    guess = initial_guess
    initial_warning = 3
    warning = initial_warning
    letters_guessed = []
    vowels = 'aeiou'
    unique_letters = ''.join(set(secret_word))  # stores only the unique letters in secret word

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warning} warnings left.')
    print('----------------')

    while guess > 0:
        print(f'You have {guess} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guessed_letter = input('Please guess a letter:').lower()

        if guessed_letter == '*':
            print(f'Possible matches are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print('----------------')

        else:
            if not guessed_letter.isalpha() and not '*':  # if user's input is not an alphabet and not '*'
                if warning != 0:
                    warning -= 1
                    print(
                        f'Oops! That is not a valid letter. You have {warning} warnings left. {get_guessed_word(secret_word, letters_guessed)}')
                else:
                    guess -= 1
                    # print('guess Line153:', guess)  # checked: all good
                    print(
                        f"Oops! That is not a valid letter. You have no warning left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                print('----------------')

            else:  # if user's input is an alphabet
                if guessed_letter in letters_guessed:  # if user has already guessed the letter
                    if warning != 0:
                        warning -= 1
                        print(
                            f"Oops! You've already guessed that letter. You have {warning} warning left: {get_guessed_word(secret_word, letters_guessed)}")
                    else:
                        guess -= 1
                        # print('guess Line162:', guess)  # checked: all good
                        print(
                            f"Oops! You've already guessed that letter. You have no warning left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                    print('----------------')
                if guessed_letter not in letters_guessed:  # if the user had not already guessed the letter
                    letters_guessed.append(guessed_letter)
                    if guessed_letter in secret_word:  # if the guessed letter is in secret word
                        print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
                    else:  # if the guessed letter is not in secret word
                        if guessed_letter in vowels:  # if the guessed word is a vowel
                            guess -= 2
                            # print('guess Line173:', guess)  # checked: all good
                        else:  # if the guessed word is not a vowel
                            guess -= 1
                            # print('guess Line176:', guess)  # checked: all good
                        print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
                    print('----------------')
                if is_word_guessed(secret_word, letters_guessed):  # if the secret word has been guessed
                    print(f'Congratulations, you won!')
                    print(f'Your total score for this game is: {guess * len(unique_letters)}')
                    break
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    # secret_word = 'apple'
    hangman_with_hints(secret_word)
