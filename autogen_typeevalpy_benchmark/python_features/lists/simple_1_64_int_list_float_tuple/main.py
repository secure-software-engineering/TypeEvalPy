# Functions are assigned as elements of a list and then called.


def func1():
    return 99


def func2():
    return [96, 74, 76]


def func3():
    return 63.98


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (12, 30, 23)


b = ["Hello"]
b[0] = func4

f = b[0]()
