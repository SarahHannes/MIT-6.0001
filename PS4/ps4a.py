# Problem Set 4A
# Name: Sarah Hannes
# Collaborators: -
# Start time: 2:42PM
# End time: 4:14PM
# Time Spent: 1:33 hours

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # create empty list to store result (result)
    result = []
    # base case: check if sequence is one character
    if len(sequence) == 1:
        return result.append(sequence)
        # append the sequence in result list and return it

    else:  # else: if the sequence is more than one character (recursive case)
        if len(sequence) == 2:  # if length of the list is equal 2
            result.append(sequence)
            result.append(sequence[-1] + sequence[0])
            return result
            # call get_permutations function on the second character (slice it)
            # append the first character at the end of the returned result
            # return the original argument and the result from previous line
        # else if the length of the list is more than 2
        elif len(sequence) > 2:
            index = 0  # index = 0
            while index != len(sequence):  # while index not equal to the length of the sequence
                a = sequence[:index]
                b = sequence[index + 1:]
                c = a + b
                perm = get_permutations(c)
                for element in perm:  # for each element in perm
                    element = sequence[index] + element
                    result.append(element)  # append the character at the index position to the start of each element, # append the appended string to result list
                index += 1  # increment index
            return result  # return result list


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))

    # example_input = 'cat'
    # print('Input:', example_input)
    # print('Expected Output:', ['cat', 'cta', 'tca', 'tac', 'act', 'atc'])
    # print('Actual Output:', get_permutations(example_input))
    # expected = ['cat', 'cta', 'tca', 'tac', 'act', 'atc']
    # actual = get_permutations(example_input)
    # print('total expected permutation: ', len(expected))
    # print('total actual permutation: ', len(actual))
    # for ele in actual:
    #     if ele not in expected:
    #         print('Incorrect')
    # print('All good! :)')

    # example_input = 'car'
    # print('Input:', example_input)
    # print('Expected Output:', ['car', 'cra', 'rca', 'rac', 'acr', 'arc'])
    # print('Actual Output:', get_permutations(example_input))
    # expected = ['car', 'cra', 'rca', 'rac', 'acr', 'arc']
    # actual = get_permutations(example_input)
    # print('total expected permutation: ', len(expected))
    # print('total actual permutation: ', len(actual))
    # for ele in actual:
    #     if ele not in expected:
    #         print('Incorrect! see:', ele)
    # print('All good! :)')

    example_input = 'sit'
    print('Input:', example_input)
    print('Expected Output:', ['sit', 'sti', 'ist', 'its', 'tsi', 'tis'])
    print('Actual Output:', get_permutations(example_input))
    expected = ['sit', 'sti', 'ist', 'its', 'tsi', 'tis']
    actual = get_permutations(example_input)
    print('total expected permutation: ', len(expected))
    print('total actual permutation: ', len(actual))
    for ele in actual:
        print(ele in expected, end=' ')



