# Functions are assigned as elements of a list and then called.


def func1():
    return (8, 94, 56)


def func2():
    return 48


def func3():
    return 'bkmvv'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 80.29


b = ["Hello"]
b[0] = func4

f = b[0]()
