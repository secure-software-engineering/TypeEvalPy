# Functions are assigned as elements of a list and then called.


def func1():
    return (71, 24, 58)


def func2():
    return [60, 56, 7]


def func3():
    return 27.66


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 68


b = ["Hello"]
b[0] = func4

f = b[0]()