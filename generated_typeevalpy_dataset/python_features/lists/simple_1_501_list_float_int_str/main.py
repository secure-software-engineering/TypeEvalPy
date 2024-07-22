# Functions are assigned as elements of a list and then called.


def func1():
    return [14, 80, 28]


def func2():
    return 30.51


def func3():
    return 60


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'iaftj'


b = ["Hello"]
b[0] = func4

f = b[0]()
