# Functions are assigned as elements of a list and then called.


def func1():
    return [11, 87, 77]


def func2():
    return 55.21


def func3():
    return 47


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (60, 59, 94)


b = ["Hello"]
b[0] = func4

f = b[0]()
