# Functions are assigned as elements of a list and then called.


def func1():
    return 71


def func2():
    return 76.74


def func3():
    return 'gyifx'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [30, 55, 15]


b = ["Hello"]
b[0] = func4

f = b[0]()
