# Problem Set 4C
# Name: Sarah Hannes
# Collaborators: None 👻
# Time Spent: 2:06 hours

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''

        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''

        copy_valid_words = self.valid_words[:]
        return copy_valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        # create empty dictionary called dict
        dict = {}
        # convert vowels_permutation to lower case
        vowels_permutation = vowels_permutation.lower()
        # for index in range the length of vowels_permutation - 1 (create dict entry for vowels)
        for index in range(len(vowels_permutation)):
            # create a dictionary entry using the vowels_lower at the index as key and vowel_permutation at the index as value
            dict[VOWELS_LOWER[index]] = vowels_permutation[index]
            # create a dictionary entry using the vowels_upper at the index as key and vowel_permutation at the index (uppercase) as value
            dict[VOWELS_UPPER[index]] = vowels_permutation[index].upper()
        # for consonants index in range the length of consonants lower - 1 (create dict entry for consonants)
        for c_index in range(len(CONSONANTS_LOWER)):
            # create a dictionary entry using the consonants lower at the index as key and the same consonants lower at the index as value
            dict[CONSONANTS_LOWER[c_index]] = CONSONANTS_LOWER[c_index]
            # create a dictionary entry using the consonants upper at the index as key and the same consonants upper at the index as value
            dict[CONSONANTS_UPPER[c_index]] = CONSONANTS_UPPER[c_index]
        # return dict
        return dict

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''

        # create an empty string to store the result
        result = ''
        # get self.message_text
        # for every element in the list
        for letter in self.message_text:
            # check if it is a letter
            if letter in string.ascii_letters:
                # get its equivalent value from the dictionary
                subs = transpose_dict[letter]
                # append the substituted letter into the result
                result = result + subs
            # if it is not a letter ie a punctuation
            else:
                # append it to the result
                result = result + letter
        # return result
        return result


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''

        # create an empty list called result
        result = []
        # create variable called valid_count, make it equal to 0
        valid_count = 0
        # get all possible permutation of vowels
        possible_perm = get_permutations('aeiou')
        # for every possible permutation
        # print('debugging possible perm:', possible_perm)
        for perm in possible_perm:
            # call build transpose dictionary (permutation), store it in dictionary variable
            dictionary = self.build_transpose_dict(perm)
            # call apply_transpose(dictionary), store it in decrypt variable
            decrypt = self.apply_transpose(dictionary)
            # split decrypt by space, store it in split_decrypt variable
            # print('debugging decrypt:', decrypt, ',using perm:', perm)
            split_decrypt = decrypt.split()
            total_words = len(split_decrypt)
            # for every word in split_decrypt variable
            for word in split_decrypt:
                # check if word.lower is in self.valid words, if it is
                if word.lower() in self.valid_words:
                    # increase valid count by 1
                    valid_count += 1
            # if valid count is more than half of the total number of words in self.message_text
            if valid_count >= (total_words//2):
                # append (decrypted message, valid_count) as a tuple to the result list
                result.append((decrypt, valid_count))
            valid_count = 0

        try:
            # get the max number of valid_count in the result list
            max_valid_count = max(l[1] for l in result)
        # except for valueError (ie in the case where result list is empty)
        except ValueError:
            # print out error message
            print('Sorry! The text could not be decrypted')
            # return the original string
            return self.message_text
        for element in result:
            if max_valid_count in element:
                return element[0]
    

if __name__ == '__main__':

    # Example test case
    # message = SubMessage("Hello World!")
    # permutation = "eaiuo"
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "Hallu Wurld!")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    # print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE

    # text = EncryptedSubMessage('thi queck brawn fax jumps avir thertiin lozy dags')
    # print('Decrypted message:', text.decrypt_message())

    text = EncryptedSubMessage('Sobstitotian ciphers encrypt the pluintext by swupping euch letter ar symbal in the pluintext by u different symbal us directed by the key. Perhups the simplest sobstitotian cipher is the Cuesur cipher, numed ufter the mun wha osed it.')
    print('Decrypted message:', text.decrypt_message())