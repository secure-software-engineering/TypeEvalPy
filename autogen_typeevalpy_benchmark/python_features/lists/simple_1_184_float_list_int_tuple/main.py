# Functions are assigned as elements of a list and then called.


def func1():
    return 94.24


def func2():
    return [17, 28, 94]


def func3():
    return 77


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (46, 42, 34)


b = ["Hello"]
b[0] = func4

f = b[0]()
