#!/bin/python3

import os
from queue import PriorityQueue


def getUmbrellas(requirement: int, sizes: list[int]) -> int:
    # Write your code here
    q = PriorityQueue()
    checked = {}
    sizes = set(sizes)
    for size in sizes:
        q.put((1, requirement - size))

    while not q.empty():
        n, rem = q.get()
        if rem == 0:
            return n
        for size in sizes:
            if rem - size < 0:
                continue
            r = rem - size
            if r not in checked or checked[r] > n + 1:
                checked[r] = n + 1
                q.put((n + 1, r))
    return -1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    requirement = int(input().strip())

    sizes_count = int(input().strip())

    sizes = []

    for _ in range(sizes_count):
        sizes_item = int(input().strip())
        sizes.append(sizes_item)

    result = getUmbrellas(requirement, sizes)

    fptr.write(str(result) + "\n")

    fptr.close()
