# A new list is created as a slice of another one containing functions.


def func1():
    return {'qfgec': 98, 'xbkdv': 96, 'hajws': 96}


def func2():
    return 72.28


def func3():
    return 'gwtog'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
