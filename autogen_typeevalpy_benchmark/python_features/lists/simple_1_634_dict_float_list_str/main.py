# Functions are assigned as elements of a list and then called.


def func1():
    return {'zwqyx': 33, 'ddzgr': 51, 'vmbgm': 7}


def func2():
    return 40.22


def func3():
    return [30, 35, 71]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'mzsuc'


b = ["Hello"]
b[0] = func4

f = b[0]()
