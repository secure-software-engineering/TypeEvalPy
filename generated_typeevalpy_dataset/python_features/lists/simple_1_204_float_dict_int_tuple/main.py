# Functions are assigned as elements of a list and then called.


def func1():
    return 91.92


def func2():
    return {'qpril': 35, 'vzagk': 99, 'ripal': 82}


def func3():
    return 35


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (24, 19, 63)


b = ["Hello"]
b[0] = func4

f = b[0]()
