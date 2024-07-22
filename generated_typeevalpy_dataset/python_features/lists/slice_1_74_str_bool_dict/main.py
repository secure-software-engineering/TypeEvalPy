# A new list is created as a slice of another one containing functions.


def func1():
    return 'vpprs'


def func2():
    return True


def func3():
    return {'vejyc': 100, 'daobr': 55, 'knafn': 86}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
