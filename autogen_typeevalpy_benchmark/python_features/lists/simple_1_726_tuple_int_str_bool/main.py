# Functions are assigned as elements of a list and then called.


def func1():
    return (24, 39, 61)


def func2():
    return 79


def func3():
    return 'ztjtr'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
