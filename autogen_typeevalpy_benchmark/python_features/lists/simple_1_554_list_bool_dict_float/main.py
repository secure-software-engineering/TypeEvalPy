# Functions are assigned as elements of a list and then called.


def func1():
    return [17, 5, 69]


def func2():
    return False


def func3():
    return {'djged': 32, 'eidsw': 23, 'fmajl': 99}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 69.48


b = ["Hello"]
b[0] = func4

f = b[0]()
