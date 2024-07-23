# A new list is created as a slice of another one containing functions.


def func1():
    return {'bsjjr': 45, 'ksllb': 68, 'gpczt': 97}


def func2():
    return 'owtjd'


def func3():
    return 48.53


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
