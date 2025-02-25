#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countPrimeStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from sys import setrecursionlimit

setrecursionlimit(10000000)


def generate_primes(end: int) -> list[bool]:
    primes = [True for prime in range(0, end + 1)]
    primes[0] = primes[1] = False
    n = 2
    while n < len(primes):
        if primes[n]:
            m = 2
            while n * m <= end:
                primes[n * m] = False
                m += 1
        n += 1
    return primes


def countPrimeStrings(s: str) -> int:
    primes = generate_primes(1000000)
    sols = [0 for _ in range(len(s) + 1)]
    sols[0] = 1
    for end in range(1, len(s) + 1):
        for stt in range(end - 1, max(-1, end - 7), -1):
            num = int(s[stt:end])
            if num > 1000000:
                break
            if s[stt] == "0":
                continue
            if primes[num]:
                sols[end] += sols[stt]
                sols[end] %= 1000000007
    return sols[-1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = countPrimeStrings(s)

    fptr.write(str(result) + "\n")

    fptr.close()
