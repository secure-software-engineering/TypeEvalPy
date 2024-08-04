# Functions are assigned as elements of a list and then called.


def func1():
    return {'csjxk': 14, 'nusub': 85, 'yvjtb': 64}


def func2():
    return [71, 87, 58]


def func3():
    return 'tzusa'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 40.71


b = ["Hello"]
b[0] = func4

f = b[0]()
