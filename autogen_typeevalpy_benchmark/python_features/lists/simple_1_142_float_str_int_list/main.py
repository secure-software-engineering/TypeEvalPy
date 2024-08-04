# Functions are assigned as elements of a list and then called.


def func1():
    return 9.09


def func2():
    return 'plwmb'


def func3():
    return 12


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [77, 11, 95]


b = ["Hello"]
b[0] = func4

f = b[0]()
