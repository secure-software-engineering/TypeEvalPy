# Functions are assigned as elements of a list and then called.


def func1():
    return 34


def func2():
    return {'xpfxw': 44, 'ppeel': 49, 'xjedq': 73}


def func3():
    return 'nzxdj'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [6, 44, 64]


b = ["Hello"]
b[0] = func4

f = b[0]()
