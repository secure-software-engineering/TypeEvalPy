# Functions are assigned as elements of a list and then called.


def func1():
    return [70, 28, 29]


def func2():
    return 89.98


def func3():
    return (9, 85, 24)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 63


b = ["Hello"]
b[0] = func4

f = b[0]()
