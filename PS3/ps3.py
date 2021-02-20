# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Sarah Hannes
# Collaborators : None 😁
# Start time    : 10/12/2020 1:55 PM
# End Time      : 10/12/2020 10:45 PM
# Time spent    : 08:50:00 😅

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 15

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    word = word.strip(' ')  # remove all spaces before and after the word
    word = word.lower()  # turn the word into all lowercase
    length = len(word)
    component1 = 0

    for letter in word:
        component1 += SCRABBLE_LETTER_VALUES[letter]

    component2 = (7 * length) - (3 * (n - length))
    if component2 < 1:
        component2 = 1

    return component1 * component2

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():           # for every letter(keys) in hand(dictionary)
        for j in range(hand[letter]):    # for the range of the values of each keys
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))  # num_vowels is the smallest integer of not less than (n/3)

    for i in range(1, num_vowels):  # for every vowel
        x = random.choice(VOWELS)  # select a random string from VOWEL (Line14)
        if x != '*':
            hand[x] = hand.get(x, 0) + 1  # check if the vowel is already exist in the dictionary, if it is return the value of the key and add 1
                                          # if the vowel did not exist in the hand dictionary, return 0 (the default value = second argument) and add 1.. put the key-value pair in the hand dictionary

    hand['*'] = 1

    for i in range(num_vowels, n):    # for every letters starting from the number of vowels = range(start, stop)
        x = random.choice(CONSONANTS)  #select a random string from CONSONANTS
        hand[x] = hand.get(x, 0) + 1  # same as above
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower()  # make all lowercase
    freq = get_frequency_dict(word)  # get the dictionary containing key(unique letters in word) -> key(num of appearance of each unique letters)
    hand_copy = hand.copy()  # copy the hand dictionary

    for key in freq:  # for each key in the freq dictionary
        if key in hand_copy:  # if the key is in hand_copy
            hand_copy[key] = hand_copy[key] - freq[key]  # update the value of the key
            if hand_copy[key] <= 0:  # if the final value is <= 0
                del(hand_copy[key])  # delete the key
        else:
            continue  # if the key is not in hand_copy, continue to the next key in sequence

    return hand_copy

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_lower = word.lower()  # make all lowercase
    word_lower.strip(' ')
    freq = get_frequency_dict(word_lower)
    list_words = []
    result = False

    for letter in word_lower:
        if letter in hand:  # if the letter is in hand
            if letter == '*':  # check if the letter is '*'
                for char in VOWELS:
                    list_words.append(word_lower.replace(letter, char)) # replace '*' with each of vowels and append all possible combination to the list

            if letter != '*':
                if freq[letter] <= hand[letter]:  # if value for freq[letter] <= hand[letter]
                    if word_lower not in list_words: # if word_lower not already in list_words
                        list_words.append(word_lower)  # append it
                else:  # if the value for freq[letter] is not <= hand[letter]
                    return False

        else:  # if the letter is not in hand
            return False

    for x in list_words:
        if x in word_list:
            result = True

    return result

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return len(hand)

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keep track of the total score
    total_score = 0
    current_hand = hand
    # As long as there are still letters left in the hand:
    while calculate_handlen(current_hand) != 0:
        # Display the hand
        print('Current Hand:', end=' ')
        display_hand(current_hand)
        # Ask user for input
        word_input = input('Enter word, or "!!" to indicate that you are finished: ').strip()
        # If the input is two exclamation points:
        if word_input == '!!':
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not two exclamation points):
        if word_input != '!!':
            # If the word is valid:
            valid = is_valid_word(word_input, current_hand, word_list)
            if valid:
                # Tell the user how many points the word earned,
                point = get_word_score(word_input, calculate_handlen(current_hand))
                print(f'"{word_input}" earned {point} points.', end=' ')
                # and the updated total score
                total_score += point
                print(f'Total score: {total_score} points')
                print()

            # Otherwise (the word is not valid):
            if not valid:
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
                print()
            # update the user's hand by removing the letters of their inputted word
            current_hand = update_hand(current_hand, word_input)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print(f'Ran out of letters. Total score: {total_score} points')

    # Return the total score as result of function
    return total_score

#
# Problem #6: Playing a game
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    # append VOWELS and CONSONANTS into alpha variable
    alphabet = VOWELS + CONSONANTS
    # copy hand dictionary into new variable
    hand_copy = hand.copy()
    # if the letter chosen is not hand dictionary
    if letter not in hand_copy:
        # do nothing, return hand dictionary
        return hand_copy
    # if the letter chosen is in hand dictionary
    if letter in hand_copy:
        # choose one alphabet at random from alpha variable
        new = random.choice(alphabet)
        # if the chosen alphabet is not in hand
        if new not in hand_copy:
            # insert the alphabet into hand_copy with value of the choosen letter (hand_copy[alphabet] = hand[letter])
            hand_copy[new] = hand[letter]
            # remove the chosen letter from hand_copy
            del(hand_copy[letter])
    # return hand_copy
    return hand_copy
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitute option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    # initialize the total score as 0 at the start of the game
    total_scores = 0
    # initialize the substitute count as 0 at the start of the game
    subs_count = 0
    # initialize the replay count as 0 at the start of the game
    replay_count = 0

    # ask the user how many times they want to play the game for
    hand_times = int(input('Enter total number of hands: ').strip(' '))
    # as long as game count is less than times the user wanted to play the game
    for i in range(hand_times):
        # deal them a hand
        current_hand = deal_hand(HAND_SIZE)
        # show them the hand
        display_hand(current_hand)
        # if substitute count is less than 1
        if subs_count < 1:
            # before playing: ask the user if they want to substitute one letter for another
            subs_input = input('Would you like to substitute a letter? ').strip(' ').lower()
            # if user inputs yes
            if subs_input == 'yes':
                # prompt them for their desired letter
                subs_letter = input('Which letter would you like to replace: ').strip(' ').lower()
                print()
                # substitute the letter for them
                # print('current hand before subs', current_hand) # for testing
                new_subs = substitute_hand(current_hand, subs_letter).copy()
                # print('new_subs', new_subs) # for testing
                # print('is new sub same as before sub', new_subs == current_hand) # for testing
                current_hand = new_subs.copy()
                # print('current hand after subs', current_hand) # for testing
                # mutate the current hand to the new substituted hand
                # increment substitute count to 1
                subs_count += 1

        # play hand using the substituted or not substituted hand
        current_score = play_hand(current_hand, word_list)
        # store the score for the current hand in current score variable

        # if replay count is less than 1
        if replay_count < 1:
            # before playing: ask the user if they would like to replay the hand
            replay_input = input('Would you like to replay the hand? ').strip(' ').lower()
            print()
            # if user inputs yes
            if replay_input == 'yes':
                # make them replay the hand
                replay_score = play_hand(current_hand, word_list)
                # if the replay score is more than the previous score of the same hand:
                if replay_score > current_score:
                    # store the replay score as the current score
                    current_score = replay_score
                    # increment replay count to 1
                    replay_count += 1

        # at the end of each hand
        # accumulate the total_score for each hand
        total_scores += current_score
        print()
        print(f'Total score for this hand: {current_score}')
        print('-------------------')
        # increment the game count by 1
    # game is over when count is equal to the times user wanted to play the game
    print(f'Total score over all hands: {total_scores}')
    # return the total score as result of function
    return total_scores


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
