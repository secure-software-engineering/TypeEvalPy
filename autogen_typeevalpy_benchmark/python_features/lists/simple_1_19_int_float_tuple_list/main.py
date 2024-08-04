# Functions are assigned as elements of a list and then called.


def func1():
    return 15


def func2():
    return 48.23


def func3():
    return (90, 21, 25)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [9, 80, 4]


b = ["Hello"]
b[0] = func4

f = b[0]()
