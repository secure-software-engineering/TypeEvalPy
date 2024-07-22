# Functions are assigned as elements of a list and then called.


def func1():
    return {'jlmil': 59, 'fgayb': 100, 'gtebm': 31}


def func2():
    return False


def func3():
    return (68, 3, 11)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 59.99


b = ["Hello"]
b[0] = func4

f = b[0]()
