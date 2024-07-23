# A new list is created as a slice of another one containing functions.


def func1():
    return {'cgzma': 15, 'ergem': 8, 'axfkj': 53}


def func2():
    return 'zddwo'


def func3():
    return 60


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
