# Functions are assigned as elements of a list and then called.


def func1():
    return 'lkgoh'


def func2():
    return {'gunxj': 94, 'sduno': 18, 'tluni': 40}


def func3():
    return 80


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (58, 99, 44)


b = ["Hello"]
b[0] = func4

f = b[0]()
