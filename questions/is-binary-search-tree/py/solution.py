from typing import Self


class node:
    data: int
    left: Self | None
    right: Self | None

    def __init__(self, data: int) -> Self:
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree_(root: node, ll: int = 0, rl: int = 10 ** 4) -> bool:
    left = root.left
    left_result = left is None
    if left:
        if left.data <= ll or left.data >= root.data:
            return False
        left_result = check_binary_search_tree_(left, ll, root.data)

    right = root.right
    right_result = right is None
    if right:
        if right.data <= root.data or right.data >= rl:
            return False
        right_result = check_binary_search_tree_(right, root.data, rl)
    return left_result and right_result
