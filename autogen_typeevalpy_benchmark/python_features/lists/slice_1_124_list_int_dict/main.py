# A new list is created as a slice of another one containing functions.


def func1():
    return [100, 94, 52]


def func2():
    return 13


def func3():
    return {'dxqmw': 79, 'rdseu': 77, 'dkafo': 24}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
