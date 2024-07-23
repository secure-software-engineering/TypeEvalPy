# Functions are assigned as elements of a list and then called.


def func1():
    return 65


def func2():
    return {'vqvgk': 40, 'uxgww': 75, 'skcsh': 85}


def func3():
    return 9.48


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cxgnq'


b = ["Hello"]
b[0] = func4

f = b[0]()
