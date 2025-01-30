#!/bin/python3

from collections import Counter
from typing import Literal
import os

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

type Result = Literal["Impossible", "Possible"]

def organizingContainers(container: list[list[int]]) -> Result:
    container_sum = Counter(sum(c) for c in container)

    n = len(container)
    ball_type_sum = Counter(sum(b[i] for b in container) for i in range(n))

    return "Possible" if container_sum == ball_type_sum else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
