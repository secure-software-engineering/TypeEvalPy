# Functions are assigned as elements of a list and then called.


def func1():
    return 92.12


def func2():
    return 56


def func3():
    return {'kugux': 98, 'niako': 9, 'edwtm': 59}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [4, 37, 61]


b = ["Hello"]
b[0] = func4

f = b[0]()
