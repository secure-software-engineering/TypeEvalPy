# Functions are assigned as elements of a list and then called.


def func1():
    return 13


def func2():
    return {'dfbbx': 1, 'wlmit': 3, 'gmpnq': 8}


def func3():
    return [4, 97, 2]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 87.77


b = ["Hello"]
b[0] = func4

f = b[0]()
