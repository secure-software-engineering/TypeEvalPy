# A new list is created as a slice of another one containing functions.


def func1():
    return {'lkymm': 86, 'midqt': 64, 'bkipm': 23}


def func2():
    return 55


def func3():
    return 'vwzsx'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
