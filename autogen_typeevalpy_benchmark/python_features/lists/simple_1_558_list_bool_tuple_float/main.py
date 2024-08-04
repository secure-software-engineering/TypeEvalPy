# Functions are assigned as elements of a list and then called.


def func1():
    return [43, 2, 39]


def func2():
    return False


def func3():
    return (36, 60, 12)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 93.23


b = ["Hello"]
b[0] = func4

f = b[0]()
