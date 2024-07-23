# A new list is created as a slice of another one containing functions.


def func1():
    return 42.55


def func2():
    return 'qvuxc'


def func3():
    return {'yjdta': 38, 'rounp': 65, 'vfnbm': 71}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
