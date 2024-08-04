# Functions are assigned as elements of a list and then called.


def func1():
    return 'skuwi'


def func2():
    return 43.14


def func3():
    return (27, 39, 68)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'fgttx': 78, 'gagyg': 42, 'myygb': 95}


b = ["Hello"]
b[0] = func4

f = b[0]()
