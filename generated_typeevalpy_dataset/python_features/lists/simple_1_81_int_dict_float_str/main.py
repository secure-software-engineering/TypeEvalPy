# Functions are assigned as elements of a list and then called.


def func1():
    return 49


def func2():
    return {'atpyz': 65, 'mofve': 20, 'wteap': 98}


def func3():
    return 91.51


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ctjqt'


b = ["Hello"]
b[0] = func4

f = b[0]()
