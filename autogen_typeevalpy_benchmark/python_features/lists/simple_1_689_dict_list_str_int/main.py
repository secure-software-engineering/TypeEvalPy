# Functions are assigned as elements of a list and then called.


def func1():
    return {'lcjoe': 100, 'zzabj': 74, 'vjpzw': 50}


def func2():
    return [94, 31, 66]


def func3():
    return 'zdhio'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 11


b = ["Hello"]
b[0] = func4

f = b[0]()
