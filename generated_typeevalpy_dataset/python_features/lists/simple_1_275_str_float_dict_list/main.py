# Functions are assigned as elements of a list and then called.


def func1():
    return 'hhlmo'


def func2():
    return 39.64


def func3():
    return {'tvpnu': 23, 'cxmhl': 83, 'bvvxr': 64}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [37, 13, 38]


b = ["Hello"]
b[0] = func4

f = b[0]()
