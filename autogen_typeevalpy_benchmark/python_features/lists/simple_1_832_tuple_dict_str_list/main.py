# Functions are assigned as elements of a list and then called.


def func1():
    return (91, 69, 89)


def func2():
    return {'idmni': 8, 'trmxs': 86, 'rmrlr': 8}


def func3():
    return 'ipnik'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [88, 9, 59]


b = ["Hello"]
b[0] = func4

f = b[0]()
