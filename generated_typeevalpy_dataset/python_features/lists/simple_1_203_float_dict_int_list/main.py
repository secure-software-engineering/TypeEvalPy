# Functions are assigned as elements of a list and then called.


def func1():
    return 39.31


def func2():
    return {'pzlzk': 1, 'nrnyx': 48, 'hhzzl': 18}


def func3():
    return 96


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [84, 40, 70]


b = ["Hello"]
b[0] = func4

f = b[0]()
