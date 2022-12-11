#!/usr/bin/env python3

import random


class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("/Users/silvanschlegel/PYCHARM/Info1/Übung 11/Word Similarity Computation/resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        from math import floor
        words = self.find_words_with_right_size()
        random.shuffle(words)
        selection = words[0:floor(len(words) / 3)]
        i = random.choice(selection)
        selection.remove(i)
        final_selection = []
        while len(final_selection) < self.num_words:
            j = random.choice(selection)
            if j not in final_selection and self.is_similar(i, j, 0.4):
                final_selection.append(j)
        return final_selection

    def is_similar(self, a, b, threshold):
        # computes similarity between a and b and shall return true if the ratio is strictly higher than threshold or false otherwise
        from difflib import SequenceMatcher

        return SequenceMatcher(None,a, b).ratio() > threshold

import time
start_time = time.time()
a = WordLogic(20, 4)
print(a.word_selection())


# my code here

print("time elapsed: {:.2f}s".format(time.time() - start_time))