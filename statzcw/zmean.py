from .zcount import zcount


def zmean(list: list) -> float:
    return sum(list)/zcount(list)



