# Functions are assigned as elements of a list and then called.


def func1():
    return 61.22


def func2():
    return 'bykip'


def func3():
    return [12, 78, 69]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'sezxc': 44, 'myeuh': 73, 'tvgbj': 74}


b = ["Hello"]
b[0] = func4

f = b[0]()
