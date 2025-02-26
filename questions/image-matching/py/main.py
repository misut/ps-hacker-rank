#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#


def regions_of(grid: list[str]) -> list[tuple[int, int]]:
    n = len(grid)
    v = [[False for _ in range(n)] for _ in range(n)]

    def adjacents_of(x: int, y: int) -> list[tuple[int, int]]:
        adjacents = []
        if x > 0:
            adjacents.append((x - 1, y))
        if x < n - 1:
            adjacents.append((x + 1, y))
        if y > 0:
            adjacents.append((x, y - 1))
        if y < n - 1:
            adjacents.append((x, y + 1))
        return adjacents

    def region_of(x: int, y: int) -> set[tuple[int, int]]:
        if v[x][y] or grid[x][y] == "0":
            return set()
        v[x][y] = True
        region = set([(x, y)])
        for ax, ay in adjacents_of(x, y):
            region = region.union(region_of(ax, ay))
        return region

    regions = []
    for x in range(n):
        for y in range(n):
            region = region_of(x, y)
            if region:
                regions.append(region)

    return regions


def countMatches(grid1: list[str], grid2: list[str]) -> int:
    regions_1 = regions_of(grid1)
    regions_2 = regions_of(grid2)

    count = 0
    for region_1 in regions_1:
        for region_2 in regions_2:
            if region_1 == region_2:
                count += 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grid1_count = int(input().strip())

    grid1 = []

    for _ in range(grid1_count):
        grid1_item = input()
        grid1.append(grid1_item)

    grid2_count = int(input().strip())

    grid2 = []

    for _ in range(grid2_count):
        grid2_item = input()
        grid2.append(grid2_item)

    result = countMatches(grid1, grid2)

    fptr.write(str(result) + "\n")

    fptr.close()
