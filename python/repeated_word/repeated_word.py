# Write a function that accepts a lengthy string parameter.
# Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

import re
import string
from hashtable.hashtable import HashTable

class Repeats:

    def __init__(self):
        self.self = self

    # def make_a_string(list_words):
    #     list_words = re.findall(r'\w+', string_input)
    #     return list_words
    
    
    def find_repeated_words(self, string_input):
        """[summary]

        Args:
            string_input ([type]): [description]

        Returns:
            [string]: [either the repeated string, or the entire unique string]
        """

        hashtable = HashTable(size=1024)
        string_input = string_input.lower().split()

        for word in string_input:
            # tried to use regex here... it didn't work so well, maybe come back to this!
            word = word.strip(str(string.punctuation))
            if hashtable.contains(word):
                return word
            else:
                hashtable.add(word, word)
                continue

        return f'String is Unique {string_input}'
    # temp = []
    # for word in list_words:
    #     temp = word[0]
    #     if temp == word:
    #         return temp
    #     elif temp != word:
    #         word + 1
    #     else:
    #         return f"String is Unique {string_input}"


# if __name__ == __main__:
