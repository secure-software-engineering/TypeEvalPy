# Functions are assigned as elements of a list and then called.


def func1():
    return 72.85


def func2():
    return True


def func3():
    return (47, 8, 91)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 51


b = ["Hello"]
b[0] = func4

f = b[0]()
