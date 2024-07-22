# Functions are assigned as elements of a list and then called.


def func1():
    return 31.15


def func2():
    return 21


def func3():
    return [21, 79, 59]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (1, 47, 20)


b = ["Hello"]
b[0] = func4

f = b[0]()
