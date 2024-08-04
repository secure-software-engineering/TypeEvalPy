# Functions are assigned as elements of a list and then called.


def func1():
    return 64.3


def func2():
    return (10, 76, 70)


def func3():
    return {'mtfei': 89, 'tcfqd': 45, 'mwqwg': 93}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ztxyl'


b = ["Hello"]
b[0] = func4

f = b[0]()
