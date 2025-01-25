#!/bin/python3

import os
from collections import Counter

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k: int, s: list[int]) -> int:
    ks = Counter(n % k for n in s)
    has_zero = 0 in ks
    is_even = k % 2 == 0

    result = int(has_zero)
    for n in range(1, k // 2 + 1):
        print(n)
        if n == k // 2 and is_even:
            result += 1
        else:
            result += max(ks[n], ks[k - n])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
