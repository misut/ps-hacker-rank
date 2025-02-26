#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getLargestString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
from collections import Counter


def getLargestString(s: str, k: int) -> str:
    # Write your code here
    result = ""
    counts = Counter(s)
    zyx = "zyxwvutsrqponmlkjihgfedcba"
    for idx, ch in enumerate(zyx):
        while counts[ch] > 0 and not result.endswith(ch * k):
            count = min(counts[ch], k)
            counts[ch] -= count
            result += ch * count
            if counts[ch] == 0:
                break
            for nx in zyx[idx + 1 :]:
                if counts[nx] > 0:
                    result += nx
                    counts[nx] -= 1
                    break
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    k = int(input().strip())

    result = getLargestString(s, k)

    fptr.write(result + "\n")

    fptr.close()
