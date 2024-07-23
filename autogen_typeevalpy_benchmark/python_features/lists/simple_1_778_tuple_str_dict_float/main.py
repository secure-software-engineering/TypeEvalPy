# Functions are assigned as elements of a list and then called.


def func1():
    return (99, 47, 75)


def func2():
    return 'rtciu'


def func3():
    return {'eihyi': 14, 'kyukr': 19, 'skanc': 87}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 15.17


b = ["Hello"]
b[0] = func4

f = b[0]()
