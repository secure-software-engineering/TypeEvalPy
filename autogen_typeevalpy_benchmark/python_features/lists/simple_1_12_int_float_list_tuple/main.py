# Functions are assigned as elements of a list and then called.


def func1():
    return 1


def func2():
    return 35.96


def func3():
    return [31, 30, 95]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (74, 40, 75)


b = ["Hello"]
b[0] = func4

f = b[0]()
