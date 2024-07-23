# Functions are assigned as elements of a list and then called.


def func1():
    return (45, 42, 7)


def func2():
    return [26, 25, 11]


def func3():
    return 54.11


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 56


b = ["Hello"]
b[0] = func4

f = b[0]()
