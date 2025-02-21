#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING encrypted
#  2. INTEGER k
#


def simpleCipher(encrypted: str, k: int) -> str:
    # Write your code here
    abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    k %= len(abc)
    dec = {c: abc[i - k] for i, c in enumerate(abc)}
    return "".join(dec[enc] for enc in encrypted)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    encrypted = input()

    k = int(input().strip())

    result = simpleCipher(encrypted, k)

    fptr.write(result + "\n")

    fptr.close()
