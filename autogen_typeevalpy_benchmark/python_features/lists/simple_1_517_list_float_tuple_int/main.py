# Functions are assigned as elements of a list and then called.


def func1():
    return [56, 46, 84]


def func2():
    return 1.47


def func3():
    return (59, 94, 15)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 13


b = ["Hello"]
b[0] = func4

f = b[0]()
