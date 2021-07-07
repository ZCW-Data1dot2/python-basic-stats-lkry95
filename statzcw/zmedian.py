from statzcw import zcount
def zmedian(list: list) -> float:
    list.sort()
    half = int(zcount(list)/2)

    if zcount(list) % 2 != 0:
        return list[half]
    elif zcount(list) % 2 == 0:
        middle = (list[half-1] + list[half]) /2
        return middle






