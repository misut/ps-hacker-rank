#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'frequency' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING s as parameter.
#


def frequency(s: str) -> list[int]:
    codes = {
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "#01": 9,
        "#11": 10,
        "#21": 11,
        "#31": 12,
        "#41": 13,
        "#51": 14,
        "#61": 15,
        "#71": 16,
        "#81": 17,
        "#91": 18,
        "#02": 19,
        "#12": 20,
        "#22": 21,
        "#32": 22,
        "#42": 23,
        "#52": 24,
        "#62": 25,
    }
    cursor = s[::-1]
    result = [0] * 26
    while cursor:
        rep = 1
        if cursor.startswith(")"):
            idx = cursor.find("(", 2)
            rep = int(cursor[idx - 1 : 0 : -1])
            cursor = cursor[idx + 1 :]
        for code, idx in codes.items():
            if cursor.startswith(code):
                result[idx] += rep
                cursor = cursor[len(code) :]
                break
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = frequency(s)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
