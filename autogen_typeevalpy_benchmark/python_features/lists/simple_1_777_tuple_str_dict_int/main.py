# Functions are assigned as elements of a list and then called.


def func1():
    return (95, 77, 40)


def func2():
    return 'htdzx'


def func3():
    return {'mfdoe': 29, 'gzgfm': 64, 'jzlqv': 70}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 44


b = ["Hello"]
b[0] = func4

f = b[0]()
