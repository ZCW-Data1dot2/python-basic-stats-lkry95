from math import sqrt
from .zmean import zmean

def zcorr(listx: list, listy: list) -> float:
    mean_x = zmean(listx)
    mean_y = zmean(listy)

    new_x = []
    for i in listx:
        new_x.append(i - mean_x)

    new_y = []
    for i in listy:
        new_y.append(i - mean_y)

    x_y_times = []
    for i, j in zip(new_x, new_y):
        x_y_times.append(i*j)

    x_times = []
    for i in new_x:
        x_times.append(i**2)

    y_times = []
    for i in new_y:
        y_times.append(i**2)

    sum_xy = sum(x_y_times)
    sum_x = sum(x_times)
    sum_y = sum(y_times)

    return sum_xy/sqrt(sum_x * sum_y)
