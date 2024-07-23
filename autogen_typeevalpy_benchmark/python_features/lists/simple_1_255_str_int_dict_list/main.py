# Functions are assigned as elements of a list and then called.


def func1():
    return 'uueod'


def func2():
    return 57


def func3():
    return {'ofoxp': 28, 'bfgbn': 39, 'accji': 33}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [57, 40, 64]


b = ["Hello"]
b[0] = func4

f = b[0]()
