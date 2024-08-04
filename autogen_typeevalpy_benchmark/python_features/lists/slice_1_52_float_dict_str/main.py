# A new list is created as a slice of another one containing functions.


def func1():
    return 43.15


def func2():
    return {'xkuxb': 12, 'wpsni': 46, 'hbcdd': 5}


def func3():
    return 'ejcwj'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
