# Functions are assigned as elements of a list and then called.


def func1():
    return (48, 47, 13)


def func2():
    return {'xxizx': 81, 'bzozx': 94, 'bbixz': 86}


def func3():
    return 73


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'pedpl'


b = ["Hello"]
b[0] = func4

f = b[0]()
