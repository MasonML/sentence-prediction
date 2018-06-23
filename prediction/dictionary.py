import os
from collections import OrderedDict

dir_path = os.path.dirname(os.path.realpath(__file__))


class Dictionary:
    def __init__(self):
        self.dictionary = self.get_dictionary()
        self.word_tuples = dict()
        self.word_pairs = dict()

    def get_dictionary(self):
        with open(dir_path + "/../datasets/words_alpha.txt") as f:
            words = f.read().split("\n")
        return {words[i]:0 for i in range(len(words))}

    def update_freq(self, word):
        try:
            self.dictionary[word] += 1
        except KeyError:
            return False
        return True

    def update_tuple_freq(self, word1, word2):
        tup = tuple((word1, word2))
        if tup not in self.word_tuples:
            self.word_tuples[tup] = 1
            if tup[0] not in self.word_pairs:
                self.word_pairs[tup[0]] = {tup[1]:1}
            else:
                self.word_pairs[tup[0]][tup[1]] = 1
        else:
            self.word_tuples[tup] += 1
            self.word_pairs[tup[0]][tup[1]] += 1

    def sorted_ordereddict(self, dct):
        return OrderedDict(dct)
