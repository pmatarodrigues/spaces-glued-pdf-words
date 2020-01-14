
import os, re
from math import log

class Model():
    def __init__(self, value_of_word, max_word_size):
        self.value_of_word = value_of_word
        self.max_word_size = max_word_size


    def split(self, s):
        letters = []
        # --- separate all the letters
        letters.append(self._split(s))

        # --- loop through all letters in part_checking
        # --- will return an array with all the letters
        return [item for sublist in letters for item in sublist]

    def best_match(self, i, cost, part_checking):
        counter = 1
        candidates = []
        # --- get a list of possible candidates from the cost of each possibility
        for total in cost[max(0, i-self.max_word_size):i]:
            candidates.append(total)
        # candidates = enumerate(cost[max(0, i-self.max_word_size):i])
        # candidates = enumerate(reversed(cost[max(0, i-self.max_word_size):i]))

        # --- for every candidate, get the word that has the lower value
        # --- which means it's the best candidate to use on this case
        position = 0
        testing = []
        result = None
        for c in candidates:
            # --- infinite is just to check that if it's None will add a huge number to the equation
            # --- so it doesn't even count later
            candidate_testing = (c + self.value_of_word.get(part_checking[i-position-1:i].lower(), float("Inf")), position+1)
            testing.append(candidate_testing)
            # --- getting the candidate with lower cost
            if result == None or candidate_testing < result:
                result = candidate_testing
            position += 1

        # --- value returning the winning candidate
        return result

    def _split(self, part_checking):
        # --- find best match for first characters
        # --- return (cost of the matched word, length of the matched word)

        # --- create an array with cost
        # --- associated to each part of the word
        cost = [0]
        for i in range(1,len(part_checking)+1):
            word_cost, word_size = self.best_match(i, cost, part_checking)
            cost.append(word_cost)

        # --- re-do all to get the part with best percentage (lower cost)
        return self.search_for_best_cost_word(part_checking, cost)


    def search_for_best_cost_word(self, part_checking, cost):
        result = []
        size_of_part_checking = len(part_checking)

        # --- run this until all the parts are checked again and the best candidate is known
        while size_of_part_checking > 0:
            word_cost, word_size = self.best_match(size_of_part_checking, cost, part_checking)

            size_remaining_part_checking = size_of_part_checking - word_size
            result.append(part_checking[size_remaining_part_checking:size_of_part_checking])

            # --- reduce the size of the total array for taking this words out
            # --- ends when there's no letters available the check
            size_of_part_checking = size_remaining_part_checking

        return reversed(result)