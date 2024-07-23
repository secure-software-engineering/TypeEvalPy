# Functions are assigned as elements of a list and then called.


def func1():
    return 'ufbsd'


def func2():
    return 22.32


def func3():
    return (91, 94, 24)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [14, 71, 78]


b = ["Hello"]
b[0] = func4

f = b[0]()
