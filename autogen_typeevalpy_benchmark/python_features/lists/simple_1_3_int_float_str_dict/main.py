# Functions are assigned as elements of a list and then called.


def func1():
    return 53


def func2():
    return 9.56


def func3():
    return 'jfrke'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vnniw': 38, 'yrldn': 10, 'faxis': 5}


b = ["Hello"]
b[0] = func4

f = b[0]()
