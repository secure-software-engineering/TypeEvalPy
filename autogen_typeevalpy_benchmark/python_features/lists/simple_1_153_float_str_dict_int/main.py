# Functions are assigned as elements of a list and then called.


def func1():
    return 38.21


def func2():
    return 'cuzpv'


def func3():
    return {'ajfmp': 73, 'jjnpc': 32, 'jvlti': 33}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 60


b = ["Hello"]
b[0] = func4

f = b[0]()
