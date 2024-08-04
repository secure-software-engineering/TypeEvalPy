# Functions are assigned as elements of a list and then called.


def func1():
    return [66, 61, 28]


def func2():
    return 29.59


def func3():
    return 'rglfs'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 59


b = ["Hello"]
b[0] = func4

f = b[0]()
