#!/bin/python3

import os

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
magic_square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]


def transpose(s: list[list[int]]) -> list[list[int]]:
    return [[s[c][r] for c in range(3)] for r in range(3)]


def rotate(s: list[list[int]], n: int) -> list[list[int]]:
    if n == 0:
        return s
    return rotate(
        [
            [s[2][0], s[1][0], s[0][0]],
            [s[2][1], s[1][1], s[0][1]],
            [s[2][2], s[1][2], s[0][2]],
        ],
        n - 1,
    )


def cost(d: list[list[int]], s: list[list[int]]) -> int:
    return sum(abs(d[c][r] - s[c][r]) for c in range(3) for r in range(3))


def formingMagicSquare(s: list[list[int]]) -> int:
    magic_squares = [rotate(magic_square, n) for n in range(4)] + [
        rotate(transpose(magic_square), n) for n in range(4)
    ]
    return min(cost(d, s) for d in magic_squares)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + "\n")

    fptr.close()
