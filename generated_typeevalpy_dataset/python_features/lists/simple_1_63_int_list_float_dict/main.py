# Functions are assigned as elements of a list and then called.


def func1():
    return 99


def func2():
    return [28, 44, 70]


def func3():
    return 25.11


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'alnje': 97, 'rtsab': 27, 'igfrs': 32}


b = ["Hello"]
b[0] = func4

f = b[0]()
