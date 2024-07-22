# Functions are assigned as elements of a list and then called.


def func1():
    return (36, 29, 29)


def func2():
    return 'wpycc'


def func3():
    return 36.64


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [13, 57, 51]


b = ["Hello"]
b[0] = func4

f = b[0]()
