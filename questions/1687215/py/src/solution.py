import math


def cross_product(x1: int, y1: int, x2: int, y2: int) -> int:
    return x1 * y2 - x2 * y1


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def vector(x1: int, y1: int, x2: int, y2: int) -> tuple[int, int]:
    return (x2 - x1, y2 - y1)


def pointsBelong(
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    x3: int,
    y3: int,
    xp: int,
    yp: int,
    xq: int,
    yq: int,
) -> int:
    ab = distance(x1, y1, x2, y2)
    bc = distance(x2, y2, x3, y3)
    ca = distance(x3, y3, x1, y1)
    if (ab + bc <= ca) or (bc + ca <= ab) or (ab + ca <= bc):
        return 0

    xp1, yp1 = vector(xp, yp, x1, y1)
    xp2, yp2 = vector(xp, yp, x2, y2)
    xp3, yp3 = vector(xp, yp, x3, y3)
    cp12 = cross_product(xp1, yp1, xp2, yp2)
    cp23 = cross_product(xp2, yp2, xp3, yp3)
    cp31 = cross_product(xp3, yp3, xp1, yp1)
    pin = (cp12 >= 0 and cp23 >= 0 and cp31 >= 0) or (
        cp12 < 0 and cp23 < 0 and cp31 < 0
    )

    xq1, yq1 = vector(xq, yq, x1, y1)
    xq2, yq2 = vector(xq, yq, x2, y2)
    xq3, yq3 = vector(xq, yq, x3, y3)
    cq12 = cross_product(xq1, yq1, xq2, yq2)
    cq23 = cross_product(xq2, yq2, xq3, yq3)
    cq31 = cross_product(xq3, yq3, xq1, yq1)
    qin = (cq12 >= 0 and cq23 >= 0 and cq31 >= 0) or (
        cq12 < 0 and cq23 < 0 and cq31 < 0
    )

    if pin and not qin:
        return 1

    if not pin and qin:
        return 2

    if pin and qin:
        return 3

    return 4
