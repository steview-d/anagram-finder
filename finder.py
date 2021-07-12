import itertools
import sys


def anagram(input_file):
    """
    Function to find anagrams of words from a given list of words

    Args:
        input_file (file): A text file containing a list of words

    Returns:
        (str): A list of found anagrams or a message indicating none found
    """

    # open text file & split into a list of words
    with open(input_file, 'r') as f:
        anagram_input = f.read()

    single_words = anagram_input.split()

    # a list of found words to stop script searching for words already
    # identified as having anagrams
    found_list = []

    # for each word, check if it is an anagram of any of the
    # other words in the list
    for word in single_words:
        if word not in found_list:
            # get all variations of the given word
            variations = list(map(''.join, itertools.permutations(word)))
            output = []
            # check to exclude words that are anagrams of only themselves
            for v in set(variations):
                if v in single_words and v != word:
                    # check for matches (anagrams) & output all matches
                    # for given word to a single line
                    for word in single_words:
                        if word in variations and word not in output:
                            output.append(word)
                            found_list.append(word)
            print(' '.join(output))

    if not found_list:
        print('no anagrams found')


def main(input_file):
    anagram(input_file)

if __name__ == "__main__":
    input_file = str(sys.argv[1])
    main(input_file)
