from statzcw import zmean

def zvariance(list: list) -> float:
    new_list = []
    for i in list:
        new_list.append((i-zmean(list))**2)
    return round(zmean(new_list),2)


