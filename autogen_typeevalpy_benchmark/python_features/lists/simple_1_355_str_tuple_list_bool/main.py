# Functions are assigned as elements of a list and then called.


def func1():
    return 'xoohb'


def func2():
    return (21, 8, 38)


def func3():
    return [69, 49, 32]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
