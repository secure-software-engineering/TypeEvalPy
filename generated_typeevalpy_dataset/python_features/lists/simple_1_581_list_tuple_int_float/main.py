# Functions are assigned as elements of a list and then called.


def func1():
    return [86, 98, 20]


def func2():
    return (69, 34, 21)


def func3():
    return 14


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 38.04


b = ["Hello"]
b[0] = func4

f = b[0]()
