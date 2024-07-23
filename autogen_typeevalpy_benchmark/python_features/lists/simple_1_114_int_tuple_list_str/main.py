# Functions are assigned as elements of a list and then called.


def func1():
    return 70


def func2():
    return (67, 81, 29)


def func3():
    return [60, 16, 16]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ukkth'


b = ["Hello"]
b[0] = func4

f = b[0]()
