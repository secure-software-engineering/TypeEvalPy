# Functions are assigned as elements of a list and then called.


def func1():
    return {'azwgd': 42, 'dxlwk': 54, 'jrnsn': 76}


def func2():
    return 1


def func3():
    return (97, 17, 93)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 56.36


b = ["Hello"]
b[0] = func4

f = b[0]()
