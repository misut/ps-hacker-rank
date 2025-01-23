#!/bin/python3

import os
from dataclasses import dataclass
from sys import setrecursionlimit
from typing import Self

setrecursionlimit(10000)

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

@dataclass
class Node:
    depth: int
    index: int
    left: Self | None = None
    right: Self | None = None

def traverse_inorder(node: Node) -> list[int]:
    result = []
    if node.left:
        result.extend(traverse_inorder(node.left))
    result.append(node.index)
    if node.right:
        result.extend(traverse_inorder(node.right))
    return result


def swap_nodes(root: Node, depth: int) -> None:
    if root.left:
        swap_nodes(root.left, depth)
    if root.right:
        swap_nodes(root.right, depth)
    if root.depth % depth == 0:
        root.left, root.right = root.right, root.left


def swapNodes(indexes: list[list[int]], queries: list[int]) -> list[list[int]]:
    root = Node(depth = 1, index = 1)
    nodes: list[Node | None] = [None] * 1025

    depth = 0
    nodes[1] = root
    for idx, (l, r) in enumerate(indexes, start=1):  # noqa: E741
        cursor = nodes[idx]
        if cursor is None:
            continue

        depth = max(cursor.depth, depth)

        if l != -1:
            lnode = Node(depth = cursor.depth + 1, index = l)
            cursor.left = lnode
            nodes[l] = lnode

        if r != -1:
            rnode = Node(depth = cursor.depth + 1, index = r)
            cursor.right = rnode
            nodes[r] = rnode

    result = []
    for query in queries:
        swap_nodes(root, query)
        result.append(traverse_inorder(root))
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
