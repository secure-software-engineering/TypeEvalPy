# A new list is created as a slice of another one containing functions.


def func1():
    return {'lkxzi': 37, 'ltbtu': 43, 'xvomu': 81}


def func2():
    return 14


def func3():
    return 46.13


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
