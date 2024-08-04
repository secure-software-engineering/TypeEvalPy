# Functions are assigned as elements of a list and then called.


def func1():
    return {'whrrb': 74, 'dxlxr': 52, 'pnwvu': 78}


def func2():
    return 'uifri'


def func3():
    return 63.11


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (41, 14, 23)


b = ["Hello"]
b[0] = func4

f = b[0]()
