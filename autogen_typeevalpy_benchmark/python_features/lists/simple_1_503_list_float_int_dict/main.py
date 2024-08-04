# Functions are assigned as elements of a list and then called.


def func1():
    return [18, 23, 79]


def func2():
    return 3.6


def func3():
    return 38


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'acalp': 67, 'vectl': 18, 'ubhge': 39}


b = ["Hello"]
b[0] = func4

f = b[0]()
