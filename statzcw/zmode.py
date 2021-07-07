def zmode(list: list) -> float:
    counter = 0
    num = list[0]

    for i in list:
        curr_freq = list.count(i)
        if(curr_freq > counter):
            counter = curr_freq
            num = i

    return num





