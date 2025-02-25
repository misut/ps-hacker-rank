#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#


def chains_of(word: str) -> list[str]:
    return [word[0:x] + word[x + 1 :] for x in range(len(word))]


def longestChain(words: list[str]) -> int:
    chain_lens = {word: 1 for word in words}
    max_chain_len = 0
    words.sort(key=lambda w: len(w))
    for word in words:
        chains = chains_of(word)
        for chain in chains:
            if chain not in chain_lens:
                continue
            chain_lens[word] = max(chain_lens[word], chain_lens[chain] + 1)
            max_chain_len = max(max_chain_len, chain_lens[word])
    return max_chain_len


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = longestChain(words)

    fptr.write(str(result) + "\n")

    fptr.close()
