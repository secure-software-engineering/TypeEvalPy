# Functions are assigned as elements of a list and then called.


def func1():
    return {'tvpho': 72, 'txmek': 61, 'kabvx': 6}


def func2():
    return 24


def func3():
    return (64, 52, 64)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'rzlst'


b = ["Hello"]
b[0] = func4

f = b[0]()
