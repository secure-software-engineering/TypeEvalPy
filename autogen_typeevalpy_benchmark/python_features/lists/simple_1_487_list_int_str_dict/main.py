# Functions are assigned as elements of a list and then called.


def func1():
    return [37, 88, 88]


def func2():
    return 6


def func3():
    return 'jwklf'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ghcvk': 94, 'gtzed': 42, 'jjkzx': 70}


b = ["Hello"]
b[0] = func4

f = b[0]()
