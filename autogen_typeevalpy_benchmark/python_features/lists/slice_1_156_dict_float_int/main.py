# A new list is created as a slice of another one containing functions.


def func1():
    return {'ymrdo': 12, 'bfntw': 73, 'onugp': 26}


def func2():
    return 81.3


def func3():
    return 71


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
