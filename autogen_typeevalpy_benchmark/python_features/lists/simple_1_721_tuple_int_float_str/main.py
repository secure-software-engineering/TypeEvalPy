# Functions are assigned as elements of a list and then called.


def func1():
    return (64, 40, 64)


def func2():
    return 76


def func3():
    return 39.26


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ruroe'


b = ["Hello"]
b[0] = func4

f = b[0]()
