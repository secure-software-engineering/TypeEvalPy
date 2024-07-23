# Functions are assigned as elements of a list and then called.


def func1():
    return 41


def func2():
    return (95, 98, 38)


def func3():
    return 'dcrep'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'casxr': 73, 'aeatr': 39, 'hawbl': 86}


b = ["Hello"]
b[0] = func4

f = b[0]()
