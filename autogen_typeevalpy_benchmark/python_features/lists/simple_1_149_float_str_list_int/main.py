# Functions are assigned as elements of a list and then called.


def func1():
    return 60.21


def func2():
    return 'jwkou'


def func3():
    return [83, 28, 35]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 47


b = ["Hello"]
b[0] = func4

f = b[0]()
