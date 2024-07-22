# Functions are assigned as elements of a list and then called.


def func1():
    return 76


def func2():
    return [81, 56, 85]


def func3():
    return 23.3


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (17, 20, 60)


b = ["Hello"]
b[0] = func4

f = b[0]()
