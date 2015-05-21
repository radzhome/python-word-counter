#!/usr/bin/env python


def cleanse_word(word):
    # find regex for word
    return word.lower().strip(',').strip('.').strip('\'').strip('"').strip('*').strip('?').strip('!').strip(';').strip(':')


class WordCounter(object):
    """ Word counting object, counts total words and top 10 occurring words """

    def __init__(self, file_path):
        self.top_10 = list()
        self.total_words = 0
        self.file_path = file_path
        self.word_freq = dict()
        self._count_words()

    def _count_words(self):
        with open(self.file_path, 'r') as f:
            for word in f.read().split():
                word = cleanse_word(word)
                self.word_freq.setdefault(word, 0)
                self.word_freq[word] += 1
                self.total_words += 1
                self._insert_to_top(word)

    def _insert_to_top(self, w):
        if self.top_10:
            for index, item in enumerate(self.top_10):
                if self.word_freq[item] <= self.word_freq[w]:
                    if w in self.top_10:
                        del self.top_10[self.top_10.index(w)]
                    self.top_10.insert(index, w)
                    del self.top_10[10:]
                    break
        else:
            self.top_10.append(w)

    def display_top_10(self):
        for word in self.top_10:
            print word, self.word_freq[word]
