# Functions are assigned as elements of a list and then called.


def func1():
    return 31


def func2():
    return 'ltepw'


def func3():
    return [88, 99, 77]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'nwwlq': 92, 'gxsmo': 20, 'cpidj': 44}


b = ["Hello"]
b[0] = func4

f = b[0]()
