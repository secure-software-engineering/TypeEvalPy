# Functions are assigned as elements of a list and then called.


def func1():
    return (73, 8, 76)


def func2():
    return 63


def func3():
    return 25.38


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [2, 57, 79]


b = ["Hello"]
b[0] = func4

f = b[0]()
