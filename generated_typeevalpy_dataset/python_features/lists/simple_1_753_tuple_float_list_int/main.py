# Functions are assigned as elements of a list and then called.


def func1():
    return (4, 1, 88)


def func2():
    return 41.48


def func3():
    return [79, 34, 88]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 76


b = ["Hello"]
b[0] = func4

f = b[0]()
