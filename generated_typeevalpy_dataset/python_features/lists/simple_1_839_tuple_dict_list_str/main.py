# Functions are assigned as elements of a list and then called.


def func1():
    return (21, 6, 67)


def func2():
    return {'movqr': 33, 'vhvqe': 4, 'cytxb': 73}


def func3():
    return [27, 95, 60]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'oupal'


b = ["Hello"]
b[0] = func4

f = b[0]()
