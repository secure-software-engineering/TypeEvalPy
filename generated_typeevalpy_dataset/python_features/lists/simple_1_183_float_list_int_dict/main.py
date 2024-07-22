# Functions are assigned as elements of a list and then called.


def func1():
    return 17.35


def func2():
    return [99, 9, 11]


def func3():
    return 61


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'oqziu': 3, 'hrvdy': 73, 'eesfu': 70}


b = ["Hello"]
b[0] = func4

f = b[0]()
