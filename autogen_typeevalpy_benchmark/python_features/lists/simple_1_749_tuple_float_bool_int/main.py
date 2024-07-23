# Functions are assigned as elements of a list and then called.


def func1():
    return (62, 74, 23)


def func2():
    return 14.62


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 44


b = ["Hello"]
b[0] = func4

f = b[0]()
