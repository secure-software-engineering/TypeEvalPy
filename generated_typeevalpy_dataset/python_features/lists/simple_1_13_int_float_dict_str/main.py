# Functions are assigned as elements of a list and then called.


def func1():
    return 61


def func2():
    return 83.16


def func3():
    return {'phbyc': 80, 'lfvbm': 79, 'idtja': 27}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ibebi'


b = ["Hello"]
b[0] = func4

f = b[0]()
