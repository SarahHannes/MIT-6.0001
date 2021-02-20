# Problem Set 4B
# Name: Sarah Hannes
# Collaborators: None 😁
# Time Start - Time End: (12:54 PM - 1:29 PM), (1:42 PM - 2:46 PM)
# Time Spent: (Part A- 1:39 hours), (Part B-1:30 hours), (Part C-1:22 hours)!! COMPLETED 😎
# Total Time Spent: 4:31 hours 😁

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        self.message_text = text.lower()
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

        valid_copy = self.valid_words[:]
        return valid_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        # create 1 empty dictionary
        dict = {}
        # store ascii upper letters in a variable
        uppers = string.ascii_uppercase
        # store ascii lower letters in a variable
        lowers = string.ascii_lowercase
        # if shift is 0
        if shift == 0:
            # map the lower case to itself and store it in dict
            for letter_low in lowers:
                dict[letter_low] = letter_low
            # map the upper case to itself and store it in dict
            for letter_up in uppers:
                dict[letter_up] = letter_up

        # else if shift is not 0
        else:
            # for each element in lower string variable
            for letter_low in lowers:
                # get the element's index position
                index = lowers.find(letter_low)
                # move the index downward according to the shift
                new_index = index + shift
                # if the resultant index is more than the len of the lower
                if new_index >= len(lowers):
                    # find the remainder of the resultant index (after subtracting 26)
                    remainder = new_index - len(lowers)
                    # move the remainder downward from the start of lower (starting from 'a')
                    new_index = remainder
                # store the mapped alphabet the its key in the dict
                dict[letter_low] = lowers[new_index]

            # for each element in upper string variable
            for letter_up in uppers:
                # get the element's index position
                index = uppers.find(letter_up)
                # move the index downward according to the shift
                new_index = index + shift
                # if the resultant index is more than the len of the upper
                if new_index >= len(uppers):
                    # find the remainder of the resultant index (after subtracting 26)
                    remainder = new_index - len(uppers)
                    # move the remainder downward from the start of upper (starting from 'A')
                    new_index = remainder
                # store the mapped alphabet the its key in the dict
                dict[letter_up] = uppers[new_index]

        # return dict
        return dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        alphabet = string.ascii_letters
        # create an empty string to store the ciphered text
        ciphered = ""
        # get the dictionary with shifted alphabet
        shift_dict = self.build_shift_dict(shift)
        # for each letter in the message_text
        for letter in self.message_text:
            # check if it is alphabet. if it is alphabet
            if letter in alphabet:
                # use it to get the value in the dictionary
                shifted_letter = shift_dict[letter]
                # append it to the ciphered text string
                ciphered = ciphered + shifted_letter
            # if it is not a string (ie punctuation)
            else:
                # append it to the ciphered text string
                ciphered = ciphered + letter
        # return the ciphered text
        return ciphered

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''

        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''

        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''

        dict_copy = self.encryption_dict.copy()
        return dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''

        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        # set the old shift value to the new shift value
        self.shift = shift
        # call the build dict function using the new shift value, save the dict to the self.dict
        self.encryption_dict = self.build_shift_dict(self.shift)
        # call the apply shift using the new shift
        self.apply_shift(self.shift)
        return None


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        # create empty list to store the result
        result = []
        # set variable called valid to be 0
        valid_count = 0
        # for the range of 1 to 26
        for index in range(1, 26):
            # apply the shift using the iterated index
            decrypt = self.apply_shift(index)
            # split the decrypted text by space
            decrypt_list = decrypt.split()
            total_words = len(decrypt_list)
            # for every word in the decrypted text
            for word in decrypt_list:
                # check if the word is valid. if it is valid (if it is a valid word, is_word returns True. so if it is valid==true, )
                # print('debugging word', word, "index", index)
                if word in self.valid_words:
                    # increment valid count
                    valid_count += 1
            # if valid is more than 0
            if valid_count >= (total_words//2):
                # append to the result list - storing in a tuple (the shift value=the iterated index, the decrypted text, the valid count)
                result.append((index, decrypt, valid_count))
            valid_count = 0

        # return tuple which have max valid count
        try:
            max_valid_count = max(l[2] for l in result) # get the max of all 3rd element of every list element in result
        # if value error (in case result is empty)
        except ValueError:
            # return 'could not ciphered!'
            print('Sorry! Could not cipher!')
            return ' '
        for ele in result: # for every list element in result
            if max_valid_count in ele:  # if max_valid_count is in the element
                return ele[0], ele[1]  # return the first element's [0] and [1] that was found


if __name__ == '__main__':

   #Example test case (PlaintextMessage)
#     plaintext = PlaintextMessage('hello', 2)
#     print('Expected Output: jgnnq')
#     print('Actual Output:', plaintext.get_message_text_encrypted())
# #
#    #Example test case (CiphertextMessage)
#     ciphertext = CiphertextMessage('jgnnq')
#     print('Expected Output:', (24, 'hello'))
#     print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
   # Example test case (PlaintextMessage)
   #  plaintext = PlaintextMessage('bed', 2)
   #  print('Expected Output: dgf')
   #  print('Actual Output:', plaintext.get_message_text_encrypted())

    #TODO: best shift value and unencrypted story
    # ciphertext = CiphertextMessage(get_story_string())
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())
    # print(ciphertext.decrypt_message())

    # cipherText = CiphertextMessage("FRRNLH")
    # print(cipherText.decrypt_message())

   # cipherText = CiphertextMessage("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")
   # print(cipherText.decrypt_message())

   cipherText = CiphertextMessage("qhqz ftagst uf xaawe xuwq gzpqoubtqdmnxq agfqd-ebmoq mxuqz fqjf, ftue iagxp fmwq mz mdy-otmud odkbfaxasuef azxk mnagf 10 yuzgfqe ad xqee fa rusgdq agf. itk? suhqz qzagst oubtqdfqjf, oqdfmuz bmffqdze nqoayq anhuage. zafuoq tai arfqz ftq qybfk ragd-eupqp naj mbbqmde: euj fuyqe agf ar m fafmx ar 29 otmdmofqde ad mnagf 20% ar ftq fuyq. ftue iagxp uyyqpumfqxk uzpuomfq ftmf ftq qybfk naj ime mxyaef oqdfmuzxk ftq ekynax rad, ftq yaef rdqcgqzfxk geqp xqffqd uz qzsxuet. aftqd xqffqde omz mxea nq pqfqdyuzqp nk ftqud rdqcgqzok mzp nk ftqud meeaoumfuaz iuft aftqd zqmdnk otmdmofqde. mxyaef mxx egnefufgfuaz oubtqde mdq abqz fa ftue wuzp ar mzmxkeue.")
   print(cipherText.decrypt_message())