#!/bin/python3

import os
from collections import Counter

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#


def matchingStrings(stringList: list[str], queries: list[str]) -> list[int]:
    counter = Counter(stringList)
    return [counter.get(query, 0) for query in queries]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
