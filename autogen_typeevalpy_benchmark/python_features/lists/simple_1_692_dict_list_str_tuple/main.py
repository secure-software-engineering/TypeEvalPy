# Functions are assigned as elements of a list and then called.


def func1():
    return {'zlflw': 27, 'xrdju': 67, 'hsbbt': 1}


def func2():
    return [33, 59, 99]


def func3():
    return 'zonsx'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (94, 99, 12)


b = ["Hello"]
b[0] = func4

f = b[0]()
