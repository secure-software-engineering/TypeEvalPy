# Functions are assigned as elements of a list and then called.


def func1():
    return 'fxikc'


def func2():
    return 66.21


def func3():
    return 27


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [84, 25, 32]


b = ["Hello"]
b[0] = func4

f = b[0]()