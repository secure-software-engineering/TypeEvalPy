# Functions are assigned as elements of a list and then called.


def func1():
    return {'pntod': 82, 'kffpl': 69, 'jtnsn': 98}


def func2():
    return 'fzmgm'


def func3():
    return 43


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 46.62


b = ["Hello"]
b[0] = func4

f = b[0]()
