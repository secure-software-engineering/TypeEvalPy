# Functions are assigned as elements of a list and then called.


def func1():
    return {'qoyuw': 94, 'mgrpr': 15, 'wtchx': 56}


def func2():
    return 'rzchy'


def func3():
    return [1, 39, 87]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 97.83


b = ["Hello"]
b[0] = func4

f = b[0]()
