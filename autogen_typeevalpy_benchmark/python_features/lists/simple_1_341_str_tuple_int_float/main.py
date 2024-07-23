# Functions are assigned as elements of a list and then called.


def func1():
    return 'gbaoc'


def func2():
    return (41, 55, 5)


def func3():
    return 48


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 76.14


b = ["Hello"]
b[0] = func4

f = b[0]()
