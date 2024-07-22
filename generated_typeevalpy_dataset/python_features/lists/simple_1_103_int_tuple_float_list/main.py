# Functions are assigned as elements of a list and then called.


def func1():
    return 61


def func2():
    return (30, 44, 34)


def func3():
    return 11.23


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [13, 86, 74]


b = ["Hello"]
b[0] = func4

f = b[0]()
