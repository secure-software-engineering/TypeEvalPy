# A new list is created as a slice of another one containing functions.


def func1():
    return 'zhdey'


def func2():
    return {'ivbds': 2, 'cggej': 61, 'ddbqz': 39}


def func3():
    return 36


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
