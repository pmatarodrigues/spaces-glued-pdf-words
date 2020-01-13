
import os, re
from math import log

class Model():
    def __init__(self, value_of_word, max_word_size):
        self.value_of_word = value_of_word
        self.max_word_size = max_word_size


    def split(self, s, regexp_to_split):
        l = [self._split(x) for x in regexp_to_split.split(s)]
        return [item for sublist in l for item in sublist]


    def _split(self, part_checking):
        # Find the best match for the i first characters, assuming cost has
        # been built for the i-1 first characters.
        # Returns a pair (match_cost, match_length).

        if(part_checking != "Atraiçoeiralínguaportuguesa"):
            return []

        def best_match(i):
            print(cost[max(0, i-self.max_word_size):i])
            candidates = enumerate(reversed(cost[max(0, i-self.max_word_size):i]))
            # for k,c in candidates:
            #     print(c)
            #     # print(self.value_of_word[part_checking[i-k-1:i].lower()] )
            #     # print(self.value_of_word.get(part_checking[i-k-1:i].lower()))
            return min((c + self.value_of_word.get(part_checking[i-k-1:i].lower(), 9e999), k+1) for k,c in candidates)

        # Build the cost array.
        cost = [0]

        for i in range(1,len(part_checking)+1):
            c,k = best_match(i)
            cost.append(c)

        # Backtrack to recover the minimal-cost string.
        out = []
        size_of_part_checking = len(part_checking) # --- i = size of the "part" checking
        while size_of_part_checking > 0:
            c, size_of_found_word = best_match(size_of_part_checking)
            # --- k = length of the word
            # --- c = cost of the word
            # assert c == cost[size_of_part_checking]
            size_remaining_part_checking = size_of_part_checking - size_of_found_word
            out.append(part_checking[size_remaining_part_checking:size_of_part_checking])

            # --- reduce the size of the total array for taking this words out
            # --- ends when there's no letters available the check
            size_of_part_checking = size_remaining_part_checking

        return reversed(out)