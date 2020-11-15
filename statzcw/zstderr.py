from math import sqrt
from statzcw import zstddev, zcount
def zstderr(list: list) -> float:
    top = zstddev(list)
    bottom = sqrt(zcount(list))
    return (round(top/bottom,2))


