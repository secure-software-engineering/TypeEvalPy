# Functions are assigned as elements of a list and then called.


def func1():
    return 3.56


def func2():
    return [6, 87, 60]


def func3():
    return 98


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (2, 11, 40)


b = ["Hello"]
b[0] = func4

f = b[0]()
