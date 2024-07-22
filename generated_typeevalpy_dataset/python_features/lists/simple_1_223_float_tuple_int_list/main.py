# Functions are assigned as elements of a list and then called.


def func1():
    return 14.61


def func2():
    return (91, 76, 15)


def func3():
    return 84


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [4, 77, 59]


b = ["Hello"]
b[0] = func4

f = b[0]()
