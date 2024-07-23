# Functions are assigned as elements of a list and then called.


def func1():
    return [86, 24, 64]


def func2():
    return 69


def func3():
    return 61.32


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (21, 77, 71)


b = ["Hello"]
b[0] = func4

f = b[0]()
