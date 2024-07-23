# Functions are assigned as elements of a list and then called.


def func1():
    return 'puita'


def func2():
    return 99.16


def func3():
    return [49, 15, 26]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 25


b = ["Hello"]
b[0] = func4

f = b[0]()
