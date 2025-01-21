#!/bin/python3

from functools import cache

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


@cache
def factorial(n: int) -> int:
    return n * factorial(n - 1) if n else 1


def extraLongFactorials(n: int) -> None:
    print(factorial(n))


if __name__ == "__main__":
    n = int(input().strip())

    extraLongFactorials(n)
