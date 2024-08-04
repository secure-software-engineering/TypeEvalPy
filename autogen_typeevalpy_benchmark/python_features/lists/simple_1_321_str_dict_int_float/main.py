# Functions are assigned as elements of a list and then called.


def func1():
    return 'wcina'


def func2():
    return {'llbyu': 84, 'tjrpz': 68, 'irvkd': 21}


def func3():
    return 29


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 85.37


b = ["Hello"]
b[0] = func4

f = b[0]()
