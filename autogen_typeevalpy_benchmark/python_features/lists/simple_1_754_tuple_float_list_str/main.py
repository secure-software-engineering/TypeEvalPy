# Functions are assigned as elements of a list and then called.


def func1():
    return (40, 69, 64)


def func2():
    return 47.95


def func3():
    return [88, 49, 6]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ccsnl'


b = ["Hello"]
b[0] = func4

f = b[0]()
