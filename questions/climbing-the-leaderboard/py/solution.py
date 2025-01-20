#!/bin/python3

import os

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    sorted_ranked = sorted(set(ranked), reverse=True)
    reversed_player = reversed(player)
    reversed_ranks = []
    rank = 1
    for score in reversed_player:
        while rank <= len(sorted_ranked) and score < sorted_ranked[rank - 1]:
            rank += 1
        reversed_ranks.append(rank)
    return reversed(reversed_ranks)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
