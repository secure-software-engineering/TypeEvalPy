# Functions are assigned as elements of a list and then called.


def func1():
    return 45


def func2():
    return {'brxik': 12, 'zftuy': 85, 'ysjvh': 55}


def func3():
    return 61.23


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'gttlh'


b = ["Hello"]
b[0] = func4

f = b[0]()
