# Functions are assigned as elements of a list and then called.


def func1():
    return {'myswk': 10, 'sqntd': 16, 'fwsey': 10}


def func2():
    return 11.28


def func3():
    return 'pyorb'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (62, 75, 73)


b = ["Hello"]
b[0] = func4

f = b[0]()
