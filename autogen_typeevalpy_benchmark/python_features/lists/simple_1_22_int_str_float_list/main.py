# Functions are assigned as elements of a list and then called.


def func1():
    return 50


def func2():
    return 'yjxhr'


def func3():
    return 32.24


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [50, 54, 59]


b = ["Hello"]
b[0] = func4

f = b[0]()
