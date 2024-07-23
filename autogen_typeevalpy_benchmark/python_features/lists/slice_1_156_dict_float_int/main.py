# A new list is created as a slice of another one containing functions.


def func1():
    return {'wioop': 54, 'mjtwo': 22, 'nwrpt': 42}


def func2():
    return 2.04


def func3():
    return 69


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
