# A new list is created as a slice of another one containing functions.


def func1():
    return {'ifeee': 32, 'nlgul': 80, 'tzynz': 17}


def func2():
    return 19.37


def func3():
    return [64, 74, 94]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
