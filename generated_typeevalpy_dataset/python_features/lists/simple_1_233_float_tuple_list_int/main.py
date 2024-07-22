# Functions are assigned as elements of a list and then called.


def func1():
    return 44.47


def func2():
    return (60, 54, 70)


def func3():
    return [97, 44, 64]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 70


b = ["Hello"]
b[0] = func4

f = b[0]()
