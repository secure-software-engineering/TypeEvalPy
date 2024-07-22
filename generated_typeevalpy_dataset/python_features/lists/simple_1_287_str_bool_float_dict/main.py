# Functions are assigned as elements of a list and then called.


def func1():
    return 'fktil'


def func2():
    return False


def func3():
    return 44.77


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'xxaia': 79, 'lcikp': 6, 'bfcoe': 95}


b = ["Hello"]
b[0] = func4

f = b[0]()
