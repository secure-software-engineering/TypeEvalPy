# Functions are assigned as elements of a list and then called.


def func1():
    return 'nltvi'


def func2():
    return [53, 56, 4]


def func3():
    return 37.64


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'eifak': 28, 'lzsdi': 15, 'tzxjg': 87}


b = ["Hello"]
b[0] = func4

f = b[0]()
