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
    anagrams = []

    # for each word, check if it is an anagram of any of the
    # other words in the list
    for word in single_words:
        variations = list(map(''.join, itertools.permutations(word)))
        variations = [v for v in variations if v != word]
        for v in set(variations):
            if v in single_words and word not in anagrams:
                anagrams.append(word)

    return ' '.join(anagrams) if anagrams else 'no anagrams found'


def main(input_file):
    print(anagram(input_file))

if __name__ == "__main__":
    input_file = str(sys.argv[1])
    main(input_file)
