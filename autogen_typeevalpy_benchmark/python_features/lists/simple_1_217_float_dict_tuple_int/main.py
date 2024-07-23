# Functions are assigned as elements of a list and then called.


def func1():
    return 15.23


def func2():
    return {'wulii': 53, 'rvytj': 32, 'zeigw': 93}


def func3():
    return (42, 4, 28)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 13


b = ["Hello"]
b[0] = func4

f = b[0]()
