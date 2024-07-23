# Functions are assigned as elements of a list and then called.


def func1():
    return 40.78


def func2():
    return 'nobsy'


def func3():
    return {'ryqki': 10, 'riomu': 24, 'zfulx': 40}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (31, 68, 1)


b = ["Hello"]
b[0] = func4

f = b[0]()
