# Functions are assigned as elements of a list and then called.


def func1():
    return (23, 97, 6)


def func2():
    return [37, 54, 96]


def func3():
    return 37.3


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'yibmb'


b = ["Hello"]
b[0] = func4

f = b[0]()
