# Functions are assigned as elements of a list and then called.


def func1():
    return {'hkowv': 50, 'txizh': 17, 'obdji': 31}


def func2():
    return 78.22


def func3():
    return 62


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [49, 51, 49]


b = ["Hello"]
b[0] = func4

f = b[0]()
