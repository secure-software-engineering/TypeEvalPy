# Functions are assigned as elements of a list and then called.


def func1():
    return 12.24


def func2():
    return {'yujvz': 27, 'dbmlm': 23, 'mekgt': 42}


def func3():
    return 'cdcey'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
