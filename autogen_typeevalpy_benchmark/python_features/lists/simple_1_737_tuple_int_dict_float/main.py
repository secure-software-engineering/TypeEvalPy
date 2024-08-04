# Functions are assigned as elements of a list and then called.


def func1():
    return (60, 86, 91)


def func2():
    return 68


def func3():
    return {'qpogo': 24, 'xlmvo': 82, 'bupak': 43}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 3.57


b = ["Hello"]
b[0] = func4

f = b[0]()
