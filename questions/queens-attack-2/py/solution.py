#!/bin/python3

import os
from sys import setrecursionlimit

setrecursionlimit(100000)

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def count(n: int, p: tuple[int, int], d: tuple[int, int], obstacles: set[tuple[int, int]]) -> int:
    rd, cd = d
    rp, cp = p
    r, c = (rd + rp, cd + cp)
    if (r < 1 or r > n) or (c < 1 or c > n):
        return 0

    np = (r, c)
    if np in obstacles:
        return 0

    return 1 + count(n, (r, c), d, obstacles)


def queensAttack(n: int, k: int, r_q: int, c_q: int, obstacles: list[list[int]]) -> int:
    ds = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    os = set((r, c) for r, c in obstacles)
    p = (r_q, c_q)
    return sum(count(n, p, d, os) for d in ds)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
