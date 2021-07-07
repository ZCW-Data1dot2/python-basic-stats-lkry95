from math import sqrt
from statzcw import zvariance
def zstddev(list: list) -> float:
    return round(sqrt(zvariance.zvariance(list)),2)



