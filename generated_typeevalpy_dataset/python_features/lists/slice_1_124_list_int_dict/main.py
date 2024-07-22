# A new list is created as a slice of another one containing functions.


def func1():
    return [14, 13, 29]


def func2():
    return 61


def func3():
    return {'zurwa': 59, 'hveqt': 65, 'wlylu': 99}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()