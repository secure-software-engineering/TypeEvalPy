# Functions are assigned as elements of a list and then called.


def func1():
    return 91.26


def func2():
    return {'ivfif': 8, 'ftpag': 42, 'szpyu': 56}


def func3():
    return (77, 94, 38)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'rltye'


b = ["Hello"]
b[0] = func4

f = b[0]()
