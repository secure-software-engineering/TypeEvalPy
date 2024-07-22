# Functions are assigned as elements of a list and then called.


def func1():
    return 79.26


def func2():
    return (95, 98, 64)


def func3():
    return 'ceump'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [85, 60, 45]


b = ["Hello"]
b[0] = func4

f = b[0]()
