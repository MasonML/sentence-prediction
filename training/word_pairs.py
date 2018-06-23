
class WordPairs:
    def __init__(self):
        self.word_tuples = dict()
        self.word_pairs = dict()

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
