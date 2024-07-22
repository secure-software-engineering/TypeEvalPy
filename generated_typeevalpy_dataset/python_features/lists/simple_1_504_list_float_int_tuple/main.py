# Functions are assigned as elements of a list and then called.


def func1():
    return [24, 64, 83]


def func2():
    return 35.56


def func3():
    return 9


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (56, 92, 57)


b = ["Hello"]
b[0] = func4

f = b[0]()
