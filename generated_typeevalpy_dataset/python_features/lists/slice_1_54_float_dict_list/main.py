# A new list is created as a slice of another one containing functions.


def func1():
    return 46.3


def func2():
    return {'ktdey': 56, 'rzbit': 51, 'aqdzt': 61}


def func3():
    return [44, 76, 74]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
