# Functions are assigned as elements of a list and then called.


def func1():
    return 43.79


def func2():
    return {'knmzd': 51, 'lkbap': 7, 'qzsxf': 16}


def func3():
    return 58


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'nrhge'


b = ["Hello"]
b[0] = func4

f = b[0]()
