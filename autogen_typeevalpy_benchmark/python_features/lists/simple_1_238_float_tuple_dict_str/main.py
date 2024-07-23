# Functions are assigned as elements of a list and then called.


def func1():
    return 33.95


def func2():
    return (12, 78, 49)


def func3():
    return {'cmeey': 8, 'fcnyt': 96, 'bgbrn': 3}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'zertl'


b = ["Hello"]
b[0] = func4

f = b[0]()
