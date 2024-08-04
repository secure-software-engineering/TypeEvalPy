# Functions are assigned as elements of a list and then called.


def func1():
    return 32.95


def func2():
    return 55


def func3():
    return {'oswob': 23, 'esqwp': 81, 'nezpd': 15}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'asptf'


b = ["Hello"]
b[0] = func4

f = b[0]()
