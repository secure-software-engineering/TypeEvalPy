# Functions are assigned as elements of a list and then called.


def func1():
    return [49, 71, 87]


def func2():
    return 52.8


def func3():
    return 68


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (48, 82, 38)


b = ["Hello"]
b[0] = func4

f = b[0]()
