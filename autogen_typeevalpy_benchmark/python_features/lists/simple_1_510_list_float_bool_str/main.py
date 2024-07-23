# Functions are assigned as elements of a list and then called.


def func1():
    return [21, 46, 87]


def func2():
    return 32.23


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'krrsf'


b = ["Hello"]
b[0] = func4

f = b[0]()
