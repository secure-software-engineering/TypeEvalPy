# Functions are assigned as elements of a list and then called.


def func1():
    return 11.15


def func2():
    return (65, 96, 6)


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [18, 44, 65]


b = ["Hello"]
b[0] = func4

f = b[0]()
