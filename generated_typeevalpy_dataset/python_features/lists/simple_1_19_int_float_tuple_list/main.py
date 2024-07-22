# Functions are assigned as elements of a list and then called.


def func1():
    return 82


def func2():
    return 85.18


def func3():
    return (22, 54, 2)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [77, 34, 68]


b = ["Hello"]
b[0] = func4

f = b[0]()
