#!/usr/bin/env python3
from random import sample
from game_logic import GameLogic


class NumberLogic(GameLogic):

    def check(self, guess):
        if len(guess) != self.len_words:
            raise Warning
        for i in range(self.len_words - 1):
            for j in range(i+1, self.len_words):
                if guess[i] == guess[j]:
                    raise Warning
        return super().check(guess)

    def _word_selection(self):
        sequences = []

        while len(sequences) < self.num_words:
            sequence = "".join(sample("0123456789", self.len_words))

            if sequence not in sequences:
                sequences.append(sequence)

        return sequences

    def _generate_feedback(self, guess):
        matching = 0
        for i in range(self.len_words):
            if guess[i] in self.password:
                matching += 1
        self.num_attempts = self.num_attempts - 1
        return "%d/%d correct" % (matching, self.len_words)


a = NumberLogic(10, 5, 7)
a.check("12345")